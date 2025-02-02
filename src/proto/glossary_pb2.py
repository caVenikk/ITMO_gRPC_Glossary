# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: glossary.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'glossary.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eglossary.proto\x12\x08glossary\"\x07\n\x05\x45mpty\"\x14\n\x06TermId\x12\n\n\x02id\x18\x01 \x01(\x05\"d\n\x0cGlossaryTerm\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04term\x18\x02 \x01(\t\x12\x12\n\ndefinition\x18\x03 \x01(\t\x12\x12\n\ncreated_at\x18\x04 \x01(\t\x12\x12\n\nupdated_at\x18\x05 \x01(\t\"9\n\x10GlossaryTermList\x12%\n\x05terms\x18\x01 \x03(\x0b\x32\x16.glossary.GlossaryTerm\"\x1e\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\"5\n\x11\x43reateTermRequest\x12\x0c\n\x04term\x18\x01 \x01(\t\x12\x12\n\ndefinition\x18\x02 \x01(\t\"A\n\x11UpdateTermRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04term\x18\x02 \x01(\t\x12\x12\n\ndefinition\x18\x03 \x01(\t\"2\n\x0e\x44\x65leteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\x8a\x03\n\x0fGlossaryService\x12:\n\x0bGetAllTerms\x12\x0f.glossary.Empty\x1a\x1a.glossary.GlossaryTermList\x12\x37\n\x0bGetTermById\x12\x10.glossary.TermId\x1a\x16.glossary.GlossaryTerm\x12\x42\n\x0bSearchTerms\x12\x17.glossary.SearchRequest\x1a\x1a.glossary.GlossaryTermList\x12\x41\n\nCreateTerm\x12\x1b.glossary.CreateTermRequest\x1a\x16.glossary.GlossaryTerm\x12\x41\n\nUpdateTerm\x12\x1b.glossary.UpdateTermRequest\x1a\x16.glossary.GlossaryTerm\x12\x38\n\nDeleteTerm\x12\x10.glossary.TermId\x1a\x18.glossary.DeleteResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'glossary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=28
  _globals['_EMPTY']._serialized_end=35
  _globals['_TERMID']._serialized_start=37
  _globals['_TERMID']._serialized_end=57
  _globals['_GLOSSARYTERM']._serialized_start=59
  _globals['_GLOSSARYTERM']._serialized_end=159
  _globals['_GLOSSARYTERMLIST']._serialized_start=161
  _globals['_GLOSSARYTERMLIST']._serialized_end=218
  _globals['_SEARCHREQUEST']._serialized_start=220
  _globals['_SEARCHREQUEST']._serialized_end=250
  _globals['_CREATETERMREQUEST']._serialized_start=252
  _globals['_CREATETERMREQUEST']._serialized_end=305
  _globals['_UPDATETERMREQUEST']._serialized_start=307
  _globals['_UPDATETERMREQUEST']._serialized_end=372
  _globals['_DELETERESPONSE']._serialized_start=374
  _globals['_DELETERESPONSE']._serialized_end=424
  _globals['_GLOSSARYSERVICE']._serialized_start=427
  _globals['_GLOSSARYSERVICE']._serialized_end=821
# @@protoc_insertion_point(module_scope)
