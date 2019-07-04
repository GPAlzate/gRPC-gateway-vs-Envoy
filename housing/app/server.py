from concurrent import futures
from app import config
from proto import registration_pb2, registration_pb2_grpc

import time, math, logging
import grpc
import psycopg2
import sys

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def create_db():
    try:
        conn = psycopg2.connect(
                user = config.USER,
                password = config.PASSWORD,
                host = config.HOST,
                port = config.PORT,
                database = config.DATABASE
                )
        conn.autocommit = True

        print(f"Connect to {config.DATABASE} successful")
        print(sys.version)
        return conn

    except:
        print("Database connection failure: Quitting...")
        return None

class RegistrationServicer(registration_pb2_grpc.RegistrationServicer): 

    def __init__(self):
        self.db = create_db()

        if self.db is None:
            return

        self.cur = self.db.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Student("
                        "id INT PRIMARY KEY,"
                        "name VARCHAR (255) NOT NULL,"
                        "dorm VARCHAR (15)NOT NULL"
                        ")")

    def CreateStudent(self, request, context):
        try:
            id = request.id
            name = request.name
            dorm = request.dorm
            self.cur.execute("INSERT INTO student (id, name, dorm) "
                    f"VALUES ({id}, {name}, {dorm})")
            student = registration_pb2.Student(id = id, name = name, dorm = dorm)
        except Exception as e:
            print(e)
            return registration_pb2.StudentResponse(student=student, ok=0)
        else:
            return registration_pb2.StudentResponse(student=student, ok=1)
    
    def ReadStudent(self, request, context):
        #get from database
        student = self.GetStudent(request)

        #respond back to client with StudentResponse
        return registration_pb2.StudentResponse(student=student, ok=1)

    def UpdateStudent(self, request, context):
        print(request.changeDorm)
        field = "dorm" if request.changeDorm else "name"
        set_new = f"UPDATE student SET {field}={request.new} WHERE id={request.id} RETURNING *"
        print(set_new)
        self.cur.execute(set_new)
        response = self.cur.fetchone()
        student = registration_pb2.Student(id=response[0], name=response[1],
                                            dorm = response[2])
        #respond back to client with StudentResponse
        return registration_pb2.StudentResponse(student=student, ok=1)

    def DeleteStudent(self, request, context):

        #delete and return
        self.cur.execute(f"DELETE FROM student WHERE id={request.id} "
                        "RETURNING *")

        response = self.cur.fetchone()
        student = registration_pb2.Student(id=response[0], name=response[1],
                                            dorm = response[2])
        #respond back to client with StudentResponse
        return registration_pb2.StudentResponse(student=student, ok=1)

    def ListStudents(self, request, context):
        self.cur.execute("SELECT * FROM student")
        rows = self.cur.fetchall()
        for row in rows:
            student = registration_pb2.Student(id=row[0], name=row[1], dorm=row[2])
            response = registration_pb2.StudentResponse(student=student, ok=1)
            yield response

    def GetStudent(self, request):
        self.cur.execute(f"SELECT * FROM student WHERE id={request.id}")
        entry = self.cur.fetchone()
        return registration_pb2.Student(id=entry[0], name=entry[1], dorm = entry[2])

    def ClearStudents(self, request, context):
        '''
        No client app for this
        '''
        self.cur.execute("TRUNCATE student")
        return registration_pb2.Void()



def serve():
    '''
    TODO: learn this cause it's just from the grpc docs idk what this does yet
    really tbh
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    registration_pb2_grpc.add_RegistrationServicer_to_server(
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

