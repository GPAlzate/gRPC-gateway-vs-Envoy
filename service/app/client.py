import grpc
import random, logging
from proto import recruiter_pb2, recruiter_pb2_grpc

NAME_PROMPT = "\nEnter your company name: "
OPEN_PROMPT = "\nHow many job openings do you have?  "
BROK_PROMPT = "\nAre you a brokerage? [y/n] "


def ClientCreateCompany(stub):
    code = random.randint(10000000,99999999)
    name = "'" + input(NAME_PROMPT) + "'"
    open = int(input(OPEN_PROMPT))
    brok = False
    if input(BROK_PROMPT) == 'y':
        brok = True

    request = recruiter_pb2.CompanyRequest(companyCode=code, companyName=name,
                                    numOpenings=open, isBrokerage=brok)
    response = stub.CreateStudent(request)

    if not response.ok:
        print("Company already exists! Please re-enter your company name\n")
    else:
        print(f"\nCreated\n{response.company}successfully.")


def ClientUpdateStudent(stub):

    #ask for id, get student
    id = int(input(ID_PROMPT))
    request = registration_pb2.StudentRequest(id=id)
    response = stub.ReadStudent(request)
    if not response.ok:
        print(f"Student with ID {request.id} does not exist!")
        return

    print(f"{response.student}")

    #ask user which field they would like to change, and change it
    request.changeDorm = int(input("Would you like to change\n"
                            "\t1) Name\n"
                            "\t2) Dorm [1, 2]? ")) - 1
    if not request.changeDorm:
        request.new = "'" + input("Please enter a new name: ") + "'"
    else:
        request.new = "'" + input("Please specify your new dorm preference: ") + "'"

    response = stub.UpdateStudent(request=request)

    print(f"{response}\nUpdated successfully")


def ClientDeleteStudent(stub):
    #keep asking for student id number to search for student to delete
    request = None
    while 1:
        id = int(input(ID_PROMPT))
        request = registration_pb2.StudentRequest(id=id)

        try:
            response = stub.ReadStudent(request)
        except grpc.RpcError as e:
            status = e.code()
            print(f"{status.name} error: {e.details()}")
            continue
        else:
            choice = input(f"Student\n{response.student}Confirm delete? [y/N] ")
            if choice != 'y':
                return

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
        stub = recruiter_pb2_grpc.RecruiterStub(channel)

        while 1:
            while 1:
                try:
                    print("\n1) Create a Company\n"
                            "2) List Housing Assignments\n"
                            "3) Edit Student Assignment\n"
                            "4) Delete Student Assignment")
                    choice = int(input("What would you like to do? [1 - 4]: "))
                except ValueError:
                    print("That is not a number. Please try again.")
                else:
                    break

            if choice == 1:
                print("\n---Create a Company---")
                ClientCreateCompany(stub)
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
