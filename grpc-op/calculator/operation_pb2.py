# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0foperation.proto\"4\n\x10OperationRequest\x12\n\n\x02op\x18\x01 \x01(\t\x12\t\n\x01\x61\x18\x02 \x01(\x05\x12\t\n\x01\x62\x18\x03 \x01(\x05\"#\n\x11OperationResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32@\n\nCalculator\x12\x32\n\tCalculate\x12\x11.OperationRequest\x1a\x12.OperationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'operation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_OPERATIONREQUEST']._serialized_start=19
  _globals['_OPERATIONREQUEST']._serialized_end=71
  _globals['_OPERATIONRESPONSE']._serialized_start=73
  _globals['_OPERATIONRESPONSE']._serialized_end=108
  _globals['_CALCULATOR']._serialized_start=110
  _globals['_CALCULATOR']._serialized_end=174
# @@protoc_insertion_point(module_scope)
