# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import recruiter_pb2 as proto_dot_recruiter__pb2


class RecruiterStub(object):
  """*
  Defines the services a client can use to register for housing.

  RPC Methods:

  CreateCompany   -   adds a new student registration

  ReadCompany     -   returns a single student from database given an
  id number

  UpdateCompany   -   updates either the name or dorm of a student given
  an id number request

  DeleteCompany   -   deletes a student given an id number request

  ListCompany     -   lists all the students in the database

  ClearCompanies   -   clears student registrations (not for client use)
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateCompany = channel.unary_unary(
        '/recruiter.Recruiter/CreateCompany',
        request_serializer=proto_dot_recruiter__pb2.Company.SerializeToString,
        response_deserializer=proto_dot_recruiter__pb2.CompanyResponse.FromString,
        )
    self.ReadCompany = channel.unary_unary(
        '/recruiter.Recruiter/ReadCompany',
        request_serializer=proto_dot_recruiter__pb2.CompanyRequest.SerializeToString,
        response_deserializer=proto_dot_recruiter__pb2.CompanyResponse.FromString,
        )
    self.UpdateCompany = channel.unary_unary(
        '/recruiter.Recruiter/UpdateCompany',
        request_serializer=proto_dot_recruiter__pb2.CompanyRequest.SerializeToString,
        response_deserializer=proto_dot_recruiter__pb2.CompanyResponse.FromString,
        )
    self.DeleteCompany = channel.unary_unary(
        '/recruiter.Recruiter/DeleteCompany',
        request_serializer=proto_dot_recruiter__pb2.CompanyRequest.SerializeToString,
        response_deserializer=proto_dot_recruiter__pb2.CompanyResponse.FromString,
        )
    self.ListCompanies = channel.unary_stream(
        '/recruiter.Recruiter/ListCompanies',
        request_serializer=proto_dot_recruiter__pb2.Void.SerializeToString,
        response_deserializer=proto_dot_recruiter__pb2.CompanyResponse.FromString,
        )
    self.ClearCompanies = channel.unary_unary(
        '/recruiter.Recruiter/ClearCompanies',
        request_serializer=proto_dot_recruiter__pb2.Void.SerializeToString,
        response_deserializer=proto_dot_recruiter__pb2.Void.FromString,
        )


class RecruiterServicer(object):
  """*
  Defines the services a client can use to register for housing.

  RPC Methods:

  CreateCompany   -   adds a new student registration

  ReadCompany     -   returns a single student from database given an
  id number

  UpdateCompany   -   updates either the name or dorm of a student given
  an id number request

  DeleteCompany   -   deletes a student given an id number request

  ListCompany     -   lists all the students in the database

  ClearCompanies   -   clears student registrations (not for client use)
  """

  def CreateCompany(self, request, context):
    """/ Creates a company from a company message. Returns created company with
    ok response
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadCompany(self, request, context):
    """/ Reads a company, queried by company code. Returns company with ok response
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateCompany(self, request, context):
    """/ Updates a student's name or dorm. Specified by `changeDorm` boolean.
    Returns new student.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteCompany(self, request, context):
    """/ Deletes a registration queried by id and returns the deleted student
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListCompanies(self, request, context):
    """/ Lists all the registered companies. Returns a stream of companies
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClearCompanies(self, request, context):
    """/ Removes all registered companies
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RecruiterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateCompany': grpc.unary_unary_rpc_method_handler(
          servicer.CreateCompany,
          request_deserializer=proto_dot_recruiter__pb2.Company.FromString,
          response_serializer=proto_dot_recruiter__pb2.CompanyResponse.SerializeToString,
      ),
      'ReadCompany': grpc.unary_unary_rpc_method_handler(
          servicer.ReadCompany,
          request_deserializer=proto_dot_recruiter__pb2.CompanyRequest.FromString,
          response_serializer=proto_dot_recruiter__pb2.CompanyResponse.SerializeToString,
      ),
      'UpdateCompany': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateCompany,
          request_deserializer=proto_dot_recruiter__pb2.CompanyRequest.FromString,
          response_serializer=proto_dot_recruiter__pb2.CompanyResponse.SerializeToString,
      ),
      'DeleteCompany': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteCompany,
          request_deserializer=proto_dot_recruiter__pb2.CompanyRequest.FromString,
          response_serializer=proto_dot_recruiter__pb2.CompanyResponse.SerializeToString,
      ),
      'ListCompanies': grpc.unary_stream_rpc_method_handler(
          servicer.ListCompanies,
          request_deserializer=proto_dot_recruiter__pb2.Void.FromString,
          response_serializer=proto_dot_recruiter__pb2.CompanyResponse.SerializeToString,
      ),
      'ClearCompanies': grpc.unary_unary_rpc_method_handler(
          servicer.ClearCompanies,
          request_deserializer=proto_dot_recruiter__pb2.Void.FromString,
          response_serializer=proto_dot_recruiter__pb2.Void.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'recruiter.Recruiter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
