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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14protocol/greet.proto\x12\x06Server\"}\n\x0cHelloRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\r\n\x05Level\x18\x02 \x01(\t\x12\x18\n\x10\x64iscriptionlevel\x18\x03 \x01(\t\x12\x10\n\x08returned\x18\x04 \x01(\t\x12\x10\n\x08\x63ontaner\x18\x05 \x01(\t\x12\x12\n\ncontanerip\x18\x06 \x01(\t\"0\n\rHelloResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x11\n\tLogStatus\x18\x02 \x01(\x05\x32\x44\n\tMyService\x12\x37\n\x08SayHello\x12\x14.Server.HelloRequest\x1a\x15.Server.HelloResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protocol.greet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=32
  _globals['_HELLOREQUEST']._serialized_end=157
  _globals['_HELLORESPONSE']._serialized_start=159
  _globals['_HELLORESPONSE']._serialized_end=207
  _globals['_MYSERVICE']._serialized_start=209
  _globals['_MYSERVICE']._serialized_end=277
# @@protoc_insertion_point(module_scope)
