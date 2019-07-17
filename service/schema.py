from graphene import ObjectType, Int, Boolean, List, String, Schema, Field
from proto import recruiter_pb2, recruiter_pb2_grpc
import json
import grpc
import random, logging, string, time

from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)
app.debug = True

class Company(ObjectType):
    companyCode = Int(required=True)
    companyName = String(required=True)
    numOpenings = Int(required=True)
    isBrokerage = Boolean(required=True)

class Query(ObjectType):
    readCompany = Field(Company, companyCode=Int())

    def resolve_readCompany(root, info,companyCode):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = recruiter_pb2_grpc.RecruiterStub(channel)
            request = recruiter_pb2.CompanyRequest(companyCode=companyCode)
            response = stub.ReadCompany(request)
            name = response.company.companyName
            ops = response.company.numOpenings
            brok = response.company.isBrokerage

            return Company(companyCode=companyCode, companyName=name,
                            numOpenings=ops, isBrokerage=brok)

schema = Schema(query=Query)
app.add_url_rule('/graphiql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
