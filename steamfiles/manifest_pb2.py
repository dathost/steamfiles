# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manifest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manifest.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0emanifest.proto\"\xae\x02\n\x07Payload\x12&\n\x08mappings\x18\x01 \x03(\x0b\x32\x14.Payload.FileMapping\x1a\xfa\x01\n\x0b\x46ileMapping\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\r\n\x05\x66lags\x18\x03 \x01(\r\x12\x14\n\x0csha_filename\x18\x04 \x01(\x0c\x12\x13\n\x0bsha_content\x18\x05 \x01(\x0c\x12.\n\x06\x63hunks\x18\x06 \x03(\x0b\x32\x1e.Payload.FileMapping.ChunkData\x1a\x61\n\tChunkData\x12\x0b\n\x03sha\x18\x01 \x01(\x0c\x12\x0b\n\x03\x63rc\x18\x02 \x01(\x07\x12\x0e\n\x06offset\x18\x03 \x01(\x04\x12\x13\n\x0b\x63\x62_original\x18\x04 \x01(\r\x12\x15\n\rcb_compressed\x18\x05 \x01(\r\"\xdd\x01\n\x08Metadata\x12\x10\n\x08\x64\x65pot_id\x18\x01 \x01(\r\x12\x14\n\x0cgid_manifest\x18\x02 \x01(\x04\x12\x15\n\rcreation_time\x18\x03 \x01(\r\x12\x1b\n\x13\x66ilenames_encrypted\x18\x04 \x01(\x08\x12\x18\n\x10\x63\x62_disk_original\x18\x05 \x01(\x04\x12\x1a\n\x12\x63\x62_disk_compressed\x18\x06 \x01(\x04\x12\x15\n\runique_chunks\x18\x07 \x01(\r\x12\x15\n\rcrc_encrypted\x18\x08 \x01(\r\x12\x11\n\tcrc_clear\x18\t \x01(\r\"\x1e\n\tSignature\x12\x11\n\tsignature\x18\x01 \x01(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PAYLOAD_FILEMAPPING_CHUNKDATA = _descriptor.Descriptor(
  name='ChunkData',
  full_name='Payload.FileMapping.ChunkData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sha', full_name='Payload.FileMapping.ChunkData.sha', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crc', full_name='Payload.FileMapping.ChunkData.crc', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='Payload.FileMapping.ChunkData.offset', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cb_original', full_name='Payload.FileMapping.ChunkData.cb_original', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cb_compressed', full_name='Payload.FileMapping.ChunkData.cb_compressed', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=321,
)

_PAYLOAD_FILEMAPPING = _descriptor.Descriptor(
  name='FileMapping',
  full_name='Payload.FileMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='Payload.FileMapping.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='Payload.FileMapping.size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='Payload.FileMapping.flags', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sha_filename', full_name='Payload.FileMapping.sha_filename', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sha_content', full_name='Payload.FileMapping.sha_content', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='Payload.FileMapping.chunks', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PAYLOAD_FILEMAPPING_CHUNKDATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=321,
)

_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mappings', full_name='Payload.mappings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PAYLOAD_FILEMAPPING, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=321,
)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='depot_id', full_name='Metadata.depot_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid_manifest', full_name='Metadata.gid_manifest', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='Metadata.creation_time', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filenames_encrypted', full_name='Metadata.filenames_encrypted', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cb_disk_original', full_name='Metadata.cb_disk_original', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cb_disk_compressed', full_name='Metadata.cb_disk_compressed', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_chunks', full_name='Metadata.unique_chunks', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crc_encrypted', full_name='Metadata.crc_encrypted', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crc_clear', full_name='Metadata.crc_clear', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=545,
)


_SIGNATURE = _descriptor.Descriptor(
  name='Signature',
  full_name='Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='Signature.signature', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=577,
)

_PAYLOAD_FILEMAPPING_CHUNKDATA.containing_type = _PAYLOAD_FILEMAPPING
_PAYLOAD_FILEMAPPING.fields_by_name['chunks'].message_type = _PAYLOAD_FILEMAPPING_CHUNKDATA
_PAYLOAD_FILEMAPPING.containing_type = _PAYLOAD
_PAYLOAD.fields_by_name['mappings'].message_type = _PAYLOAD_FILEMAPPING
DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['Signature'] = _SIGNATURE

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(

  FileMapping = _reflection.GeneratedProtocolMessageType('FileMapping', (_message.Message,), dict(

    ChunkData = _reflection.GeneratedProtocolMessageType('ChunkData', (_message.Message,), dict(
      DESCRIPTOR = _PAYLOAD_FILEMAPPING_CHUNKDATA,
      __module__ = 'manifest_pb2'
      # @@protoc_insertion_point(class_scope:Payload.FileMapping.ChunkData)
      ))
    ,
    DESCRIPTOR = _PAYLOAD_FILEMAPPING,
    __module__ = 'manifest_pb2'
    # @@protoc_insertion_point(class_scope:Payload.FileMapping)
    ))
  ,
  DESCRIPTOR = _PAYLOAD,
  __module__ = 'manifest_pb2'
  # @@protoc_insertion_point(class_scope:Payload)
  ))
_sym_db.RegisterMessage(Payload)
_sym_db.RegisterMessage(Payload.FileMapping)
_sym_db.RegisterMessage(Payload.FileMapping.ChunkData)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'manifest_pb2'
  # @@protoc_insertion_point(class_scope:Metadata)
  ))
_sym_db.RegisterMessage(Metadata)

Signature = _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATURE,
  __module__ = 'manifest_pb2'
  # @@protoc_insertion_point(class_scope:Signature)
  ))
_sym_db.RegisterMessage(Signature)


# @@protoc_insertion_point(module_scope)
