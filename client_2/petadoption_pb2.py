# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: petadoption.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'petadoption.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11petadoption.proto\x12\x0bpetadoption\"T\n\x07PetInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06gender\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\r\n\x05\x62reed\x18\x04 \x01(\t\x12\x0f\n\x07picture\x18\x05 \x01(\x0c\"8\n\x14RegistrationResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1e\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\"-\n\x07PetList\x12\"\n\x04pets\x18\x01 \x03(\x0b\x32\x14.petadoption.PetInfo2\x9b\x01\n\x12PetAdoptionService\x12\x46\n\x0bRegisterPet\x12\x14.petadoption.PetInfo\x1a!.petadoption.RegistrationResponse\x12=\n\tSearchPet\x12\x1a.petadoption.SearchRequest\x1a\x14.petadoption.PetListB2\n\x1cio.grpc.examples.petadoptionB\x10PetAdoptionProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'petadoption_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034io.grpc.examples.petadoptionB\020PetAdoptionProtoP\001'
  _globals['_PETINFO']._serialized_start=34
  _globals['_PETINFO']._serialized_end=118
  _globals['_REGISTRATIONRESPONSE']._serialized_start=120
  _globals['_REGISTRATIONRESPONSE']._serialized_end=176
  _globals['_SEARCHREQUEST']._serialized_start=178
  _globals['_SEARCHREQUEST']._serialized_end=208
  _globals['_PETLIST']._serialized_start=210
  _globals['_PETLIST']._serialized_end=255
  _globals['_PETADOPTIONSERVICE']._serialized_start=258
  _globals['_PETADOPTIONSERVICE']._serialized_end=413
# @@protoc_insertion_point(module_scope)
