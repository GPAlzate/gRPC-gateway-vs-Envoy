import grpc
import random, logging, string
from proto import recruiter_pb2, recruiter_pb2_grpc

CODE_PROMPT = "\nEnter your provided company code: "
NAME_PROMPT = "Enter your company name: "
OPEN_PROMPT = "How many job openings do you have?  "
BROK_PROMPT = "Are you a brokerage? [y/N] "

_CHARS = string.ascii_letters

def ClientCreateCompany(stub):
    """ DEMO: add company to database

    Adds a company to the database of hiring companies. For locust testing
    purposes, generate a random id number to test for concurrency issues
    
    Args:
        stub    - uses the stub to call server code of the same type
    """

    # testing purposes, generate random ID number
    code = random.randint(10000000,99999999)
    name = "'" + input('\n' + NAME_PROMPT) + "'"
    ops = int(input('\n'+OPEN_PROMPT))
    brok = False
    if input('\n'+BROK_PROMPT) == 'y':
        brok = True

    # make grpc request and delegate to server CreateCompany
    request = recruiter_pb2.Company(companyCode=code, companyName=name,
                                    numOpenings=ops, isBrokerage=brok)
    response = stub.CreateCompany(request)

    if not response.ok:
        print("Company already exists! Please re-enter your company name\n")
    else:
        print(f"\nCreated\n{response.company}successfully.")


def ClientUpdateCompany(stub):
    """ DEMO: update existing company in database

    Change any or all of company name, number, job openings, or payment package.
    
    Args:
        stub    - uses the stub to call server code of the same type
    """

    # delegate to CompanyRequest to fetch a company from database, keep asking
    # if it doesn't exist
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
            break

    # print company name
    comp = response.company
    print(comp)

    # control flow to change company attributes
    if input("Would you like to update the company name? [y/N] ") == 'y':
        request.companyName = f"'{input('NAME UPDATE: ' + NAME_PROMPT)}'"
    else:
        request.companyName = f"'{comp.companyName}'"

    if input("Would you like to update the number of openings? [y/N] ") == 'y':
        request.numOpenings = int(input("NUM. OPEN. UPDATE: " + OPEN_PROMPT))
    else:
        request.numOpenings = comp.numOpenings

    if comp.isBrokerage:
        print("You are currently registered as a brokerage.", end = " ")
    else:
        print("You are currently not registered as a brokerage.", end = " ")

    if input("Would you like to update brokerage status? [y/N] ") == 'y':
        request.isBrokerage = not comp.isBrokerage
    else:
        request.isBrokerage = comp.isBrokerage

    # update company attributes in database
    request.ok=True
    response = stub.UpdateCompany(request)

    if not response.ok:
        print("Error! Something went wrong with the database. Please try again")
    else:
        print(f"{response}\nUpdated successfully")


def ClientDeleteCompany(stub):
    """ DEMO: delete company in database

    Deletes a selected company (keyed by ID) from the database
    
    Args:
        stub    - uses the stub to call server code of the same type
    """

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
    """ DEMO: list all companies in database

    Makes use of server-side streaming RPC (as opposed to simple RPC) to list
    all companies in database
    
    Args:
        stub    - uses the stub to call server code of the same type
    """

    # some void objectt since ListCompanies takes in no argument
    void = recruiter_pb2.Void()
    responses = stub.ListCompanies(void)

    # iterate through RPC stream and print out company
    for response in responses:
        company = response.company
        print(f"Code: {company.companyCode} | Name: {company.companyName} | "
                f"Openings: {company.numOpenings} | Brokerage: {company.isBrokerage}")

def run():
    """ The 'main' method to run the client demo

    Opens a channel to the GRPC server app and allows the user to:
        - create,
        - list,
        - edit, and
        - delete a company from the database
    """
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = recruiter_pb2_grpc.RecruiterStub(channel)

        while 1:
            try:
                print("\n1) Create a Company\n"
                        "2) List Registered Companies\n"
                        "3) Edit Company\n"
                        "4) Delete Company")
                choice = int(input("What would you like to do? [1 - 4]: "))
            except ValueError:
                print("That is not a number. Please try again.")
                continue

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
