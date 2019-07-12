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

class RegistrationServicer(recruiter_pb2_grpc.RegistrationServicer): 

    def __init__(self):
        self.db = create_db()

        if self.db is None:
            return

        self.cur = self.db.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS companies("
                        "companyCode INT PRIMARY KEY,"
                        "companyName VARCHAR (255) NOT NULL,"
                        "numOpenings INT (15) NOT NULL CHECK(numOpenings > 0),"
                        "isBrokerage BOOLEAN NOT NULL"
                        ")")

    def CreateCompany(self, request, context):
        try:
            code = request.companyCode
            name = request.companyName
            ops = request.numOpenings
            broks = request.isBrokerage
            company = recruiter_pb2.Company(companyCode = code, companyName = name,
                                            numOpenings = ops, isBrokerage = broks)

            with _lock:
                try:
                    self.cur.execute("INSERT INTO companies (companyCode, companyName, "
                                        "numOpenings, isBrokerage) "
                                        f"VALUES ({code}, {name}, {ops}, {broks})")
                except psycopg2.IntegrityError:
                    self.db.rollback()
                    return recruiter_pb2.CompanyResponse(company=company, ok=0)
                else:
                    self.db.commit()
                    return recruiter_pb2.CompanyResponse(company=company, ok=0)
        except Exception as e:
            print(str(e))
    
    def ReadCompany(self, request, context):
        #get from database via helper method
        student = self.GetCompany(request)

        #400 if the requested student doesn't exist
        if not student.id:
            context.set_details(f"Student with ID {request.id} does not exist!")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return recruiter_pb2.StudentResponse(student=student, ok=0)

        return recruiter_pb2.StudentResponse(student=student, ok=1)

    def UpdateCompany(self, request, context):
        '''
        id = request.id
        name = ''.join(random.sample(_CHARS, 8)) + " " + ''.join(random.sample(_CHARS, 8))
        dorm = ''.join(random.sample(_CHARS, 12)) 
        if request.changeDorm:
            dorm = request.new
        else:
            name = request.new
        student = recruiter_pb2.Student(id = id, name = name, dorm = dorm)
        return recruiter_pb2.StudentResponse(student=student, ok=1) 

        '''

        try:
            field = "dorm" if request.changeDorm else "name"
            set_new = f"UPDATE student SET {field}={request.new} WHERE id={request.id} RETURNING *"

            with _lock:
                try:
                    self.cur.execute(set_new)
                    response = self.cur.fetchone()
                    if response is None:
                        context.set_details(f"Student with ID {request.id} does not exist!")
                        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                        student = recruiter_pb2.Student(id=0)
                        return recruiter_pb2.StudentResponse(student=student, ok=0)

                    self.db.commit()
                    student = recruiter_pb2.Student(id=response[0], name=response[1],
                                                        dorm=response[2])
                    #respond back to client with StudentResponse
                    return recruiter_pb2.StudentResponse(student=student, ok=1)
                except Exception as e:
                    print(str(e))
        except Exception as e:
            print(str(e))

    def DeleteCompany(self, request, context):
        try:

            with _lock:
                #delete and return
                self.cur.execute(f"DELETE FROM student WHERE id={request.id} "
                                "RETURNING *")
                response = self.cur.fetchone()

                #400 response
                if response is None:
                    context.set_details(f"Student with ID {request.id} does not exist!!")
                    context.set_code(grpc.StatusCode.UNKNOWN)
                    badstudent = recruiter_pb2.Student()
                    return recruiter_pb2.StudentResponse(student=badstudent, ok=0)

                self.db.commit()
                student = recruiter_pb2.Student(id=response[0], name=response[1],
                                                    dorm = response[2])
                #respond back to client with StudentResponse
                return recruiter_pb2.StudentResponse(student=student, ok=1)
        except Exception as e:
            print(str(e))

    def ListCompanies(self, request, context):

        '''
        for _ in range(random.randint(100, 1000)):
            id = random.randint(10000000, 99999999)
            name = ''.join(random.sample(_CHARS, 8)) + " " + ''.join(random.sample(_CHARS, 8))
            dorm = ''.join(random.sample(_CHARS, 12))
            student = recruiter_pb2.Student(id=id, name=name, dorm=dorm) 
            yield recruiter_pb2.StudentResponse(student=student, ok=1)

        '''

        try:
            with _lock:
                self.cur.execute("SELECT * FROM student")
                rows = self.cur.fetchall()
                for row in rows:
                    student = recruiter_pb2.Student(id=row[0], name=row[1], dorm=row[2])
                    response = recruiter_pb2.StudentResponse(student=student, ok=1)
                    yield response
        except Exception as e:
            print(str(e))

    def GetCompany(self, request):
        '''
        name = ''.join(random.sample(_CHARS, 8)) + " " + ''.join(random.sample(_CHARS, 8))
        dorm = ''.join(random.sample(_CHARS, 12))
        return recruiter_pb2.Student(id=request.id, name=name, dorm=dorm)

        '''
        try:
            with _lock:
                self.cur.execute(f"SELECT * FROM student WHERE id={request.id}")
                entry = self.cur.fetchone()
                if entry is None:
                    return recruiter_pb2.Student(id=0)
                return recruiter_pb2.Student(id=entry[0], name=entry[1], dorm=entry[2])
        except Exception as e:
            print(str(e))

    def ClearCompanies(self, request, context):
        '''
        No client app for this
        '''
        self.cur.execute("TRUNCATE student")
        self.db.commit()
        return recruiter_pb2.Void()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recruiter_pb2_grpc.add_RegistrationServicer_to_server(
            RegistrationServicer(), server)
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

