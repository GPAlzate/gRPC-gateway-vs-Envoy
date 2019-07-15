from graphene import ObjectType, ID, Int, Boolean, List, String, Schema
import json

_COMPANIES_QUERY = '''
    query nameAndCode {
        companies {
            companyCode
            companyName
        }
    }
    query allInfo {
        companies {
            companyCode
            companyName
            numOpenings
            isBrokerage
        }
    }
'''

class Company(ObjectType):
    companyCode = ID(required=True, default_value = 0)
    companyName = String(required=True, default_value = "Error")
    numOpenings = Int(default_value = 255)
    isBrokerage = Boolean(default_value = False)


class Query(ObjectType):

    #retrieves only the code and the name
    companies = List(Company)

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_companies(root, info):
        return [
            Company(companyCode=10357854, companyName="Google", numOpenings=47, isBrokerage=True),
            Company(companyCode=31415962, companyName="Kalibrr", numOpenings=21, isBrokerage=True),
            Company(companyCode=65358979, companyName="Nintendo", numOpenings=10, isBrokerage=True),
            Company(companyCode=32384626, companyName="Eskwelabs", numOpenings=3, isBrokerage=False),
        ]


schema = Schema(query=Query)
result = schema.execute(_COMPANIES_QUERY, operation_name = 'nameAndCode')
print(json.dumps(dict(result.data), indent = 4))
