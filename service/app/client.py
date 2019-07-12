import grpc
import random, logging, string
from proto import recruiter_pb2, recruiter_pb2_grpc

CODE_PROMPT = "\nEnter your provided company code: "
NAME_PROMPT = "\nEnter your company name: "
OPEN_PROMPT = "\nHow many job openings do you have?  "
BROK_PROMPT = "\nAre you a brokerage? [y/n] "

_CHARS = string.ascii_letters
def ClientCreateCompany(stub):
    code = random.randint(10000000,99999999)
    name = "'" + input(NAME_PROMPT) + "'"
    ops = int(input(OPEN_PROMPT))
    brok = False
    if input(BROK_PROMPT) == 'y':
        brok = True

    request = recruiter_pb2.Company(companyCode=code, companyName=name,
                                    numOpenings=ops, isBrokerage=brok)
    response = stub.CreateCompany(request)

    if not response.ok:
        print("Company already exists! Please re-enter your company name\n")
    else:
        print(f"\nCreated\n{response.company}successfully.")


def ClientUpdateCompany(stub):
    """
        BIG TODO: fix architecture of this thing

    code = int(input(CODE_PROMPT))
    request = recruiter_pb2.CompanyRequest(companyCode=code)
    response = stub.ReadCompany(request)
    if not response.ok:
        print(f"Company with code {request.companyCode} does not exist!")
        return

    print(f"{response.company}")

    #ask user which field they would like to change, and change it
    choice = int(input("Would you like to change\n"
                            "\t1) Name\n"
                            "\t2) Number of openings\n"
                            "\t3) Brokerage status [1, 2, 3]? ")) - 1
    if choice == 1:
        request.new = "'" + input("Please enter a new name: ") + "'"
    elif choice == 2:
        request.new = "'" + input("Please specify your new dorm preference: ") + "'"

    response = stub.UpdateStudent(request=request)

    print(f"{response}\nUpdated successfully")
    """

    code = 10357854
    name = "'" + ''.join(random.sample(_CHARS, 12)) + "'"
    ops = random.randint(1, 99)
    brok = None

    request = recruiter_pb2.CompanyRequest(companyCode=code, companyName=name,
                                    numOpenings=ops, isBrokerage=brok)
    response = stub.UpdateCompany(request)
    print(f"{response.company}\nUpdated successfully")

def ClientDeleteCompany(stub):
    #keep asking for provided company code to search for company to delete
    request = None
    while 1:
        code = int(input(CODE_PROMPT))
        request = recruiter_pb2.CompanyRequest(companyCode=code)

        try:
            response = stub.ReadCompany(request)
        except grpc.RpcError as e:
            status = e.code()
            print(f"{status.name} error: {e.details()}")
            continue
        else:
            choice = input(f"---Company---\n{response.company}Confirm delete? [y/N] ")
            if choice != 'y':
                continue
            break

    print("Deleting...")
    response = stub.DeleteCompany(request)
    print(f"\nDeleted\n{response.company}successfully.")

def ClientListCompanies(stub):
    void = recruiter_pb2.Void()
    responses = stub.ListCompanies(void)
    for response in responses:
        company = response.company
        print(f"Code: {company.companyCode} | Name: {company.companyName} | "
                f"Openings: {company.numOpenings} | Brokerage: {company.isBrokerage}")

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = recruiter_pb2_grpc.RecruiterStub(channel)

        while 1:
            while 1:
                try:
                    print("\n1) Create a Company\n"
                            "2) List Registered Companies\n"
                            "3) Edit Company\n"
                            "4) Delete Company")
                    choice = int(input("What would you like to do? [1 - 4]: "))
                except ValueError:
                    print("That is not a number. Please try again.")
                else:
                    break

            if choice == 1:
                print("\n---Create a Company---")
                ClientCreateCompany(stub)
            elif choice == 2:
                print("\n---List Registered Companies---\n")
                ClientListCompanies(stub)
            elif choice == 3:
                print("\n---Edit Company---")
                ClientUpdateCompany(stub)
            else:
                print("\n---Delete Company---")
                ClientDeleteCompany(stub)

if __name__ == '__main__':
    run()
