# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncomm.proto\"\x1a\n\x07Request\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x18\n\x05Reply\x12\x0f\n\x07message\x18\x01 \x01(\t2}\n\x04\x43omm\x12%\n\rTransfer_CtoS\x12\x08.Request\x1a\x06.Reply\"\x00(\x01\x12%\n\rTransfer_StoC\x12\x08.Request\x1a\x06.Reply\"\x00\x30\x01\x12\'\n\rTransfer_Both\x12\x08.Request\x1a\x06.Reply\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'comm_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=14
  _globals['_REQUEST']._serialized_end=40
  _globals['_REPLY']._serialized_start=42
  _globals['_REPLY']._serialized_end=66
  _globals['_COMM']._serialized_start=68
  _globals['_COMM']._serialized_end=193
# @@protoc_insertion_point(module_scope)