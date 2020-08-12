# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: country.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='country.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcountry.proto\"\x0e\n\x0c\x43ountryEmpty\";\n\x17\x43ountryMultipleResponse\x12 \n\x07\x63ountry\x18\x01 \x03(\x0b\x32\x0f.CountryRequest\"f\n\x0e\x43ountryRequest\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x14\n\x0cphone_prefix\x18\x03 \x02(\t\x12\x14\n\x06\x61\x63tive\x18\x04 \x01(\x08:\x04true\x12\x0e\n\x06states\x18\x05 \x03(\t2=\n\x07\x43ountry\x12\x32\n\x07get_all\x12\r.CountryEmpty\x1a\x18.CountryMultipleResponse'
)




_COUNTRYEMPTY = _descriptor.Descriptor(
  name='CountryEmpty',
  full_name='CountryEmpty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=31,
)


_COUNTRYMULTIPLERESPONSE = _descriptor.Descriptor(
  name='CountryMultipleResponse',
  full_name='CountryMultipleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='country', full_name='CountryMultipleResponse.country', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=92,
)


_COUNTRYREQUEST = _descriptor.Descriptor(
  name='CountryRequest',
  full_name='CountryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CountryRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='CountryRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_prefix', full_name='CountryRequest.phone_prefix', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='CountryRequest.active', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='states', full_name='CountryRequest.states', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=196,
)

_COUNTRYMULTIPLERESPONSE.fields_by_name['country'].message_type = _COUNTRYREQUEST
DESCRIPTOR.message_types_by_name['CountryEmpty'] = _COUNTRYEMPTY
DESCRIPTOR.message_types_by_name['CountryMultipleResponse'] = _COUNTRYMULTIPLERESPONSE
DESCRIPTOR.message_types_by_name['CountryRequest'] = _COUNTRYREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CountryEmpty = _reflection.GeneratedProtocolMessageType('CountryEmpty', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYEMPTY,
  '__module__' : 'country_pb2'
  # @@protoc_insertion_point(class_scope:CountryEmpty)
  })
_sym_db.RegisterMessage(CountryEmpty)

CountryMultipleResponse = _reflection.GeneratedProtocolMessageType('CountryMultipleResponse', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYMULTIPLERESPONSE,
  '__module__' : 'country_pb2'
  # @@protoc_insertion_point(class_scope:CountryMultipleResponse)
  })
_sym_db.RegisterMessage(CountryMultipleResponse)

CountryRequest = _reflection.GeneratedProtocolMessageType('CountryRequest', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYREQUEST,
  '__module__' : 'country_pb2'
  # @@protoc_insertion_point(class_scope:CountryRequest)
  })
_sym_db.RegisterMessage(CountryRequest)



_COUNTRY = _descriptor.ServiceDescriptor(
  name='Country',
  full_name='Country',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=198,
  serialized_end=259,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_all',
    full_name='Country.get_all',
    index=0,
    containing_service=None,
    input_type=_COUNTRYEMPTY,
    output_type=_COUNTRYMULTIPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COUNTRY)

DESCRIPTOR.services_by_name['Country'] = _COUNTRY

# @@protoc_insertion_point(module_scope)
