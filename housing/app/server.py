from concurrent import futures
from app import config
from proto import registration_pb2, registration_pb2_grpc
import threading

import time, math, logging
import grpc
import psycopg2
import sys, random, string, math

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

        id = request.id
        name = request.name
        dorm = request.dorm
        student = registration_pb2.Student(id = id, name = name, dorm = dorm)
        return registration_pb2.StudentResponse(student=student, ok=1)

        '''
        try:
            id = request.id
            name = request.name
            dorm = request.dorm
            student = registration_pb2.Student(id = id, name = name, dorm = dorm)

            with _lock:
                try:
                    self.cur.execute("INSERT INTO student (id, name, dorm) "
                            f"VALUES ({id}, {name}, {dorm})")
                except psycopg2.IntegrityError:
                    self.db.rollback()
                    return registration_pb2.StudentResponse(student=student, ok=0)
                else:
                    self.db.commit()
                    return registration_pb2.StudentResponse(student=student, ok=1)
        except Exception as e:
            print(str(e))
        '''
    
    def ReadStudent(self, request, context):
        #get from database via helper method
        student = self.GetStudent(request)

        if not student.id:
            return registration_pb2.StudentResponse(student=student, ok=0)

        return registration_pb2.StudentResponse(student=student, ok=1)

    def UpdateStudent(self, request, context):

        id = request.id
        name = ''.join(random.sample(_CHARS, 8)) + " " + ''.join(random.sample(_CHARS, 8))
        dorm = ''.join(random.sample(_CHARS, 12)) 
        if request.changeDorm:
            dorm = request.new
        else:
            name = request.new
        student = registration_pb2.Student(id = id, name = name, dorm = dorm)
        return registration_pb2.StudentResponse(student=student, ok=1) 

        '''
        try:
            field = "dorm" if request.changeDorm else "name"
            set_new = f"UPDATE student SET {field}={request.new} WHERE id={request.id} RETURNING *"

            with _lock:
                try:
                    self.cur.execute(set_new)
                    response = self.cur.fetchone()
                    if response is None:
                        student = registration_pb2.Student(id=0, name="ID does not exist!", dorm="ERROR")
                        return registration_pb2.StudentResponse(student=student, ok=0)

                    self.db.commit()
                    student = registration_pb2.Student(id=response[0], name=response[1],
                                                        dorm=response[2])
                    #respond back to client with StudentResponse
                    return registration_pb2.StudentResponse(student=student, ok=1)
        except Exception as e:
            print(str(e))
        '''

    def DeleteStudent(self, request, context):

        name = ''.join(random.sample(_CHARS, 8)) + " " + ''.join(random.sample(_CHARS, 8))
        dorm = ''.join(random.sample(_CHARS, 12))
        student = registration_pb2.Student(id=request.id, name=name, dorm=dorm) 
        return registration_pb2.StudentResponse(student=student, ok=1)

        '''
        try:
            with _lock:
                #delete and return
                self.cur.execute(f"DELETE FROM student WHERE id={request.id} "
                                "RETURNING *")
                response = self.cur.fetchone()
                if response is None:
                    student = registration_pb2.Student(id=0, name="ID does not exist!", dorm="ERROR")
                    return registration_pb2.StudentResponse(student=student, ok=0)

                self.db.commit()
                student = registration_pb2.Student(id=response[0], name=response[1],
                                                    dorm = response[2])
                #respond back to client with StudentResponse
                return registration_pb2.StudentResponse(student=student, ok=1)
        except Exception as e:
            print(str(e))
            '''

    def ListStudents(self, request, context):

        for _ in range(random.randint(100, 1000)):
            id = random.randint(10000000, 99999999)
            name = ''.join(random.sample(_CHARS, 8)) + " " + ''.join(random.sample(_CHARS, 8))
            dorm = ''.join(random.sample(_CHARS, 12))
            student = registration_pb2.Student(id=id, name=name, dorm=dorm) 
            yield registration_pb2.StudentResponse(student=student, ok=1)

        '''
        try:
            with _lock:
                self.cur.execute("SELECT * FROM student")
                rows = self.cur.fetchall()
                for row in rows:
                    student = registration_pb2.Student(id=row[0], name=row[1], dorm=row[2])
                    response = registration_pb2.StudentResponse(student=student, ok=1)
                    yield response
        except Exception as e:
            print(str(e))
            '''

    def GetStudent(self, request):

        name = ''.join(random.sample(_CHARS, 8)) + " " + ''.join(random.sample(_CHARS, 8))
        dorm = ''.join(random.sample(_CHARS, 12))
        return registration_pb2.Student(id=request.id, name=name, dorm=dorm)

        '''
        try:
            with _lock:
                self.cur.execute(f"SELECT * FROM student WHERE id={request.id}")
                entry = self.cur.fetchone()
                if entry is None:
                    return registration_pb2.Student(id=0, name="ERROR", dorm="ERROR")
                return registration_pb2.Student(id=entry[0], name=entry[1], dorm=entry[2])
        except Exception as e:
            print(str(e))
        '''

    def ClearStudents(self, request, context):
        '''
        No client app for this
        '''
        self.cur.execute("TRUNCATE student")
        self.db.commit()
        return registration_pb2.Void()


def serve():
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

