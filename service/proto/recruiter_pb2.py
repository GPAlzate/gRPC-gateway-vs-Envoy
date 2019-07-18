# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/recruiter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/recruiter.proto',
  package='recruiter',
  syntax='proto3',
  serialized_options=_b('\222A\341\001\022D\n=Simple demo CRUD app for companies hiring on Kalibrr platform2\0031.0*\001\0012\020application/json:\020application/jsonR5\n\003400\022.\n$Returned when the ID does not exist.\022\006\n\004\232\002\001\007R\035\n\003502\022\026\n\014Server Error\022\006\n\004\232\002\001\007R\034\n\003503\022\025\n\013Bad Gateway\022\006\n\004\232\002\001\007'),
  serialized_pb=_b('\n\x15proto/recruiter.proto\x12\trecruiter\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\"\x06\n\x04Void\"]\n\x07\x43ompany\x12\x13\n\x0b\x63ompanyCode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63ompanyName\x18\x02 \x01(\t\x12\x13\n\x0bnumOpenings\x18\x03 \x01(\x05\x12\x13\n\x0bisBrokerage\x18\x04 \x01(\x08\"p\n\x0e\x43ompanyRequest\x12\x13\n\x0b\x63ompanyCode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63ompanyName\x18\x02 \x01(\t\x12\x13\n\x0bnumOpenings\x18\x03 \x01(\x05\x12\x13\n\x0bisBrokerage\x18\x04 \x01(\x08\x12\n\n\x02ok\x18\x05 \x01(\x08\"B\n\x0f\x43ompanyResponse\x12#\n\x07\x63ompany\x18\x01 \x01(\x0b\x32\x12.recruiter.Company\x12\n\n\x02ok\x18\x02 \x01(\x08\x32\xaa\x07\n\tRecruiter\x12\x9b\x01\n\rCreateCompany\x12\x12.recruiter.Company\x1a\x1a.recruiter.CompanyResponse\"Z\x82\xd3\xe4\x93\x02\x0e\"\t/register:\x01*\x92\x41\x43\x12\rSummary: test\x1a\x10\x44\x65scription TestJ \n\x03\x32\x30\x30\x12\x19\n\x0fOverwrites YEET\x12\x06\n\x04\x9a\x02\x01\x07\x12\xf9\x01\n\x0bReadCompany\x12\x19.recruiter.CompanyRequest\x1a\x1a.recruiter.CompanyResponse\"\xb2\x01\x82\xd3\xe4\x93\x02\x1a\x12\x18/companies/{companyCode}\x92\x41\x8e\x01\x12-Company is not in the database. Cannot delete\x1a*Company with {companyCode} does not exist!J1\n\x03\x34\x30\x30\x12*\n Overwrites default when deleting\x12\x06\n\x04\x9a\x02\x01\x07\x12h\n\rUpdateCompany\x12\x19.recruiter.CompanyRequest\x1a\x1a.recruiter.CompanyResponse\" \x82\xd3\xe4\x93\x02\x1a\x1a\x15/update/{companyCode}:\x01*\x12\x80\x02\n\rDeleteCompany\x12\x19.recruiter.CompanyRequest\x1a\x1a.recruiter.CompanyResponse\"\xb7\x01\x82\xd3\xe4\x93\x02\x17*\x15/delete/{companyCode}\x92\x41\x96\x01\x12\x35ID has not been registered for housing. Cannot delete\x1a*Company with {companyCode} does not exist!J1\n\x03\x34\x30\x30\x12*\n Overwrites default when deleting\x12\x06\n\x04\x9a\x02\x01\x07\x12R\n\rListCompanies\x12\x0f.recruiter.Void\x1a\x1a.recruiter.CompanyResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/companies0\x01\x12\x42\n\x0e\x43learCompanies\x12\x0f.recruiter.Void\x1a\x0f.recruiter.Void\"\x0e\x82\xd3\xe4\x93\x02\x08*\x06/clearB\xe5\x01\x92\x41\xe1\x01\x12\x44\n=Simple demo CRUD app for companies hiring on Kalibrr platform2\x03\x31.0*\x01\x01\x32\x10\x61pplication/json:\x10\x61pplication/jsonR5\n\x03\x34\x30\x30\x12.\n$Returned when the ID does not exist.\x12\x06\n\x04\x9a\x02\x01\x07R\x1d\n\x03\x35\x30\x32\x12\x16\n\x0cServer Error\x12\x06\n\x04\x9a\x02\x01\x07R\x1c\n\x03\x35\x30\x33\x12\x15\n\x0b\x42\x61\x64 Gateway\x12\x06\n\x04\x9a\x02\x01\x07\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,])




_VOID = _descriptor.Descriptor(
  name='Void',
  full_name='recruiter.Void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=118,
)


_COMPANY = _descriptor.Descriptor(
  name='Company',
  full_name='recruiter.Company',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='companyCode', full_name='recruiter.Company.companyCode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='companyName', full_name='recruiter.Company.companyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numOpenings', full_name='recruiter.Company.numOpenings', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isBrokerage', full_name='recruiter.Company.isBrokerage', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=213,
)


_COMPANYREQUEST = _descriptor.Descriptor(
  name='CompanyRequest',
  full_name='recruiter.CompanyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='companyCode', full_name='recruiter.CompanyRequest.companyCode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='companyName', full_name='recruiter.CompanyRequest.companyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numOpenings', full_name='recruiter.CompanyRequest.numOpenings', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isBrokerage', full_name='recruiter.CompanyRequest.isBrokerage', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ok', full_name='recruiter.CompanyRequest.ok', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=327,
)


_COMPANYRESPONSE = _descriptor.Descriptor(
  name='CompanyResponse',
  full_name='recruiter.CompanyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='company', full_name='recruiter.CompanyResponse.company', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ok', full_name='recruiter.CompanyResponse.ok', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=395,
)

_COMPANYRESPONSE.fields_by_name['company'].message_type = _COMPANY
DESCRIPTOR.message_types_by_name['Void'] = _VOID
DESCRIPTOR.message_types_by_name['Company'] = _COMPANY
DESCRIPTOR.message_types_by_name['CompanyRequest'] = _COMPANYREQUEST
DESCRIPTOR.message_types_by_name['CompanyResponse'] = _COMPANYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), dict(
  DESCRIPTOR = _VOID,
  __module__ = 'proto.recruiter_pb2'
  # @@protoc_insertion_point(class_scope:recruiter.Void)
  ))
_sym_db.RegisterMessage(Void)

Company = _reflection.GeneratedProtocolMessageType('Company', (_message.Message,), dict(
  DESCRIPTOR = _COMPANY,
  __module__ = 'proto.recruiter_pb2'
  # @@protoc_insertion_point(class_scope:recruiter.Company)
  ))
_sym_db.RegisterMessage(Company)

CompanyRequest = _reflection.GeneratedProtocolMessageType('CompanyRequest', (_message.Message,), dict(
  DESCRIPTOR = _COMPANYREQUEST,
  __module__ = 'proto.recruiter_pb2'
  # @@protoc_insertion_point(class_scope:recruiter.CompanyRequest)
  ))
_sym_db.RegisterMessage(CompanyRequest)

CompanyResponse = _reflection.GeneratedProtocolMessageType('CompanyResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMPANYRESPONSE,
  __module__ = 'proto.recruiter_pb2'
  # @@protoc_insertion_point(class_scope:recruiter.CompanyResponse)
  ))
_sym_db.RegisterMessage(CompanyResponse)


DESCRIPTOR._options = None

_RECRUITER = _descriptor.ServiceDescriptor(
  name='Recruiter',
  full_name='recruiter.Recruiter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=398,
  serialized_end=1336,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateCompany',
    full_name='recruiter.Recruiter.CreateCompany',
    index=0,
    containing_service=None,
    input_type=_COMPANY,
    output_type=_COMPANYRESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\"\t/register:\001*\222AC\022\rSummary: test\032\020Description TestJ \n\003200\022\031\n\017Overwrites YEET\022\006\n\004\232\002\001\007'),
  ),
  _descriptor.MethodDescriptor(
    name='ReadCompany',
    full_name='recruiter.Recruiter.ReadCompany',
    index=1,
    containing_service=None,
    input_type=_COMPANYREQUEST,
    output_type=_COMPANYRESPONSE,
    serialized_options=_b('\202\323\344\223\002\032\022\030/companies/{companyCode}\222A\216\001\022-Company is not in the database. Cannot delete\032*Company with {companyCode} does not exist!J1\n\003400\022*\n Overwrites default when deleting\022\006\n\004\232\002\001\007'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateCompany',
    full_name='recruiter.Recruiter.UpdateCompany',
    index=2,
    containing_service=None,
    input_type=_COMPANYREQUEST,
    output_type=_COMPANYRESPONSE,
    serialized_options=_b('\202\323\344\223\002\032\032\025/update/{companyCode}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteCompany',
    full_name='recruiter.Recruiter.DeleteCompany',
    index=3,
    containing_service=None,
    input_type=_COMPANYREQUEST,
    output_type=_COMPANYRESPONSE,
    serialized_options=_b('\202\323\344\223\002\027*\025/delete/{companyCode}\222A\226\001\0225ID has not been registered for housing. Cannot delete\032*Company with {companyCode} does not exist!J1\n\003400\022*\n Overwrites default when deleting\022\006\n\004\232\002\001\007'),
  ),
  _descriptor.MethodDescriptor(
    name='ListCompanies',
    full_name='recruiter.Recruiter.ListCompanies',
    index=4,
    containing_service=None,
    input_type=_VOID,
    output_type=_COMPANYRESPONSE,
    serialized_options=_b('\202\323\344\223\002\014\022\n/companies'),
  ),
  _descriptor.MethodDescriptor(
    name='ClearCompanies',
    full_name='recruiter.Recruiter.ClearCompanies',
    index=5,
    containing_service=None,
    input_type=_VOID,
    output_type=_VOID,
    serialized_options=_b('\202\323\344\223\002\010*\006/clear'),
  ),
])
_sym_db.RegisterServiceDescriptor(_RECRUITER)

DESCRIPTOR.services_by_name['Recruiter'] = _RECRUITER

# @@protoc_insertion_point(module_scope)
