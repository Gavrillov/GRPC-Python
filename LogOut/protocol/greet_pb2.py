# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol/greet.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14protocol/greet.proto\x12\x06Server\"e\n\x0cHelloRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05Level\x18\x02 \x01(\t\x12\x18\n\x10\x64iscriptionlevel\x18\x03 \x01(\t\x12\x10\n\x08returned\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\" \n\rHelloResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2D\n\tMyService\x12\x37\n\x08SayHello\x12\x14.Server.HelloRequest\x1a\x15.Server.HelloResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protocol.greet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=32
  _globals['_HELLOREQUEST']._serialized_end=133
  _globals['_HELLORESPONSE']._serialized_start=135
  _globals['_HELLORESPONSE']._serialized_end=167
  _globals['_MYSERVICE']._serialized_start=169
  _globals['_MYSERVICE']._serialized_end=237
# @@protoc_insertion_point(module_scope)
