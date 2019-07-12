from concurrent import futures
from app import config
from proto import recruiter_pb2, recruiter_pb2_grpc
import threading

import time, math, logging
import grpc
import psycopg2
import sys, random, string

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_CHARS = string.ascii_letters

_lock = threading.Lock()

def create_db():
    try:
        conn = psycopg2.connect(
                user = config.USER,
                password = config.PASSWORD,
                host = config.HOST,
                port = config.PORT,
                database = config.DATABASE
                )

        print(f"Connect to {config.DATABASE} successful")
        print(sys.version)
        return conn

    except:
        print("Database connection failure: Quitting...")
        return None

class RecruiterServicer(recruiter_pb2_grpc.RecruiterServicer): 

    def __init__(self):
        self.db = create_db()

        if self.db is None:
            return

        self.cur = self.db.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS companies("
                        "companyCode INT PRIMARY KEY,"
                        "companyName VARCHAR (255) NOT NULL,"
                        "numOpenings INT NOT NULL CHECK(numOpenings > 0),"
                        "isBrokerage BOOLEAN NOT NULL"
                        ")")

    def CreateCompany(self, request, context):
        """
            Registers a company in the Kalibrr database. Will return a not OK
            response for any errors.
        """
        try:
            #make new company request
            code = request.companyCode
            name = request.companyName
            ops = request.numOpenings
            brok = request.isBrokerage

            company = recruiter_pb2.Company(companyCode = code,
                    companyName = name, numOpenings = ops, isBrokerage = brok)

            #insert new company in a thread safe manner
            with _lock:
                try:
                    self.cur.execute("INSERT INTO companies (companyCode, companyName, "
                                        "numOpenings, isBrokerage) "
                                        f"VALUES ({code}, {name}, {ops}, {brok})")
                except psycopg2.IntegrityError:
                    self.db.rollback()
                    return recruiter_pb2.CompanyResponse(company=company)
                else:
                    self.db.commit()
                    return recruiter_pb2.CompanyResponse(company=company, ok=1)
        except Exception as e:
            print(str(e))
    
    def ReadCompany(self, request, context):
        """
            Gets a company from the Kalibrr database, queried by a unique
            company code.
        """
        #get from database via helper method
        company = self.GetCompany(request)

        #400 if the requested company doesn't exist
        if not company.companyCode:
            context.set_details(f"Company with code {request.companyCode} does not exist!")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return recruiter_pb2.CompanyResponse(company=company, ok=0)

        return recruiter_pb2.CompanyResponse(company=company, ok=1)

    def UpdateCompany(self, request, context):
        """
            Allows changes to be made to a registered company. Can change the
            company name or the number of job openings.
        """
        try:
            code = request.companyCode
            name = request.companyName
            ops = request.numOpenings
            brok = request.isBrokerage

            setNewFields = "SET "
            if name:
                setNewFields += f"companyName={name},"
            if ops:
                setNewFields += f"numOpenings={ops},"
            if brok is not None:
                setNewFields += f"isBrokerage={brok}"

            set_new = f"UPDATE companies {setNewFields.rstrip(',')} WHERE companyCode={code} RETURNING *"

            with _lock:
                self.cur.execute(set_new)
                response = self.cur.fetchone()
                return self.SubmitResponse(code, response, context)
        except Exception as e:
            print(str(e))

    def DeleteCompany(self, request, context):
        try:
            code = request.companyCode
            with _lock:
                #delete and return
                self.cur.execute(f"DELETE FROM companies "
                                f"WHERE companyCode={code} RETURNING *")
                response = self.cur.fetchone()
                return self.SubmitResponse(code, response, context)
        except Exception as e:
            print(str(e))

    def ListCompanies(self, request, context):
        try:
            with _lock:
                self.cur.execute("SELECT * FROM companies")
                rows = self.cur.fetchall()
                for row in rows:
                    company = recruiter_pb2.Company(companyCode=row[0], companyName=row[1],
                                                numOpenings=row[2], isBrokerage=row[3])
                    yield recruiter_pb2.CompanyResponse(company=company, ok=1)
        except Exception as e:
            print(str(e))

    def GetCompany(self, request):
        """
            Helper method gets one company from the database, queried by unique code
        """
        try:
            with _lock:
                self.cur.execute(f"SELECT * FROM companies WHERE " 
                                    f"companyCode={request.companyCode}")
                entry = self.cur.fetchone()

                #returns with company code 0 by default
                if entry is None:
                    return recruiter_pb2.Company()
                return recruiter_pb2.Company(companyCode=entry[0], companyName=entry[1],
                                            numOpenings=entry[2], isBrokerage=entry[3])
        except Exception as e:
            print(str(e))

    def ClearCompanies(self, request, context):
        """
            No client app for this; clears the entire database of companies. For
            testing purposes only
        """
        self.cur.execute("TRUNCATE companies")
        self.db.commit()
        return recruiter_pb2.Void()

    def SubmitResponse(self, code, response, context):
        #400 response
        if response is None:
            context.set_details(f"Company with code {code} does not exist!")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            company = recruiter_pb2.Company()
            return recruiter_pb2.CompanyResponse(company=company, ok=0)

        self.db.commit()
        company = recruiter_pb2.Company(companyCode=response[0], companyName=response[1],
                                    numOpenings=response[2], isBrokerage=response[3])
        return recruiter_pb2.CompanyResponse(company=company, ok=1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recruiter_pb2_grpc.add_RecruiterServicer_to_server(
            RecruiterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while 1:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    logging.basicConfig()
    serve()

