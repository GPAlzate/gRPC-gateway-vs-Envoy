import grpc
import random, logging
from proto import registration_pb2, registration_pb2_grpc

ID_PROMPT = "\nEnter your id (8-digit number): "
NAME_PROMPT = "Enter your name (first and last): "
DORM_PROMPT = "\nEnter a dorm: "

def ClientCreateStudent(stub):
    name = "'" + input(NAME_PROMPT) + "'"
    id = int(input(ID_PROMPT))
    dorm = "'" + input(DORM_PROMPT) + "'"

    request = registration_pb2.Student(name = name, id = id, dorm = dorm)
    response = stub.CreateStudent(request)
    print(f"\nCreated\n{response.student}successfully.")


def ClientUpdateStudent(stub):

    #ask for id, get student
    id = int(input(ID_PROMPT))
    request = registration_pb2.StudentRequest(id=id)
    print(f"{stub.ReadStudent(request).student}")

    #ask user which field they would like to change, and change it
    request.changeDorm = int(input("Would you like to change\n"
                            "\t1) Name\n"
                            "\t2) Dorm [1, 2]? ")) - 1
    if not request.changeDorm:
        request.new = "'" + input("Please enter a new name: ") + "'"
    else:
        request.new = "'" + input("Please specify your new dorm preference: ") + "'"

    print(f"{stub.UpdateStudent(request=request)}\nUpdated successfully")


def ClientDeleteStudent(stub):
    #keep asking for student id number to search for student to delete
    request = None
    while 1:
        id = int(input(ID_PROMPT))
        request = registration_pb2.StudentRequest(id=id)
        response = stub.ReadStudent(request)
        choice = input(f"Student\n{response.student}Confirm delete? [y/N] ")
        if choice == 'y':
            break

    response = stub.DeleteStudent(request)
    print(f"\nDeleted\n{response.student}successfully.")

def ClientListStudents(stub):
    void = registration_pb2.Void()
    responses = stub.ListStudents(void)
    for response in responses:
        student = response.student
        print(f"ID: {student.id} | Name: {student.name} | Dorm: {student.dorm} ")



def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = registration_pb2_grpc.RegistrationStub(channel)

        while 1:
            while 1:
                try:
                    print("\n1) Assign a Student\n"
                            "2) List Housing Assignments\n"
                            "3) Edit Student Assignment\n"
                            "4) Delete Student Assignment")
                    choice = int(input("What would you like to do? [1 - 4]: "))
                except ValueError:
                    print("That is not a number. Please try again.")
                else:
                    break

            if choice == 1:
                print("\n---Assign a Student---")
                ClientCreateStudent(stub)
            elif choice == 2:
                print("\n---List Housing Assignments---\n")
                ClientListStudents(stub)
            elif choice == 3:
                print("\n---Edit Student Assignment---")
                ClientUpdateStudent(stub)
            else:
                print("\n---Delete Student Assignment---")
                ClientDeleteStudent(stub)

if __name__ == '__main__':
    run()
