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
  serialized_pb=b'\n\rcountry.proto\"\x0e\n\x0c\x43ountryEmpty\"2\n\x07\x43itiesC\x12\n\n\x02id\x18\x01 \x02(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"M\n\x06States\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x18\n\x06\x63ities\x18\x04 \x03(\x0b\x32\x08.CitiesC\"o\n\x0e\x43ountryRequest\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x14\n\x0cphone_prefix\x18\x03 \x02(\t\x12\x14\n\x06\x61\x63tive\x18\x04 \x01(\x08:\x04true\x12\x17\n\x06states\x18\x05 \x03(\x0b\x32\x07.States\"I\n\x13\x43ountryTableRequest\x12\x0c\n\x04page\x18\x01 \x02(\x05\x12\x14\n\x08per_page\x18\x02 \x01(\x05:\x02\x31\x35\x12\x0e\n\x06search\x18\x03 \x01(\t\";\n\x17\x43ountryMultipleResponse\x12 \n\x07\x63ountry\x18\x01 \x03(\x0b\x32\x0f.CountryRequest\"~\n\x14\x43ountryTableResponse\x12\x1e\n\x05items\x18\x01 \x03(\x0b\x32\x0f.CountryRequest\x12\x0c\n\x04page\x18\x02 \x02(\x05\x12\x10\n\x08per_page\x18\x03 \x02(\x05\x12\x13\n\x0btotal_items\x18\x04 \x02(\x05\x12\x11\n\tnum_pages\x18\x05 \x02(\x05\x32s\n\x07\x43ountry\x12\x34\n\x05table\x12\x14.CountryTableRequest\x1a\x15.CountryTableResponse\x12\x32\n\x07get_all\x12\r.CountryEmpty\x1a\x18.CountryMultipleResponse'
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


_CITIESC = _descriptor.Descriptor(
  name='CitiesC',
  full_name='CitiesC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CitiesC.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='CitiesC.state', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='CitiesC.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_end=83,
)


_STATES = _descriptor.Descriptor(
  name='States',
  full_name='States',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='States.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='States.country', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='States.name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cities', full_name='States.cities', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=85,
  serialized_end=162,
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
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=164,
  serialized_end=275,
)


_COUNTRYTABLEREQUEST = _descriptor.Descriptor(
  name='CountryTableRequest',
  full_name='CountryTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='CountryTableRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='CountryTableRequest.per_page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=15,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search', full_name='CountryTableRequest.search', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=277,
  serialized_end=350,
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
  serialized_start=352,
  serialized_end=411,
)


_COUNTRYTABLERESPONSE = _descriptor.Descriptor(
  name='CountryTableResponse',
  full_name='CountryTableResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='CountryTableResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='CountryTableResponse.page', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='CountryTableResponse.per_page', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_items', full_name='CountryTableResponse.total_items', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_pages', full_name='CountryTableResponse.num_pages', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=413,
  serialized_end=539,
)

_STATES.fields_by_name['cities'].message_type = _CITIESC
_COUNTRYREQUEST.fields_by_name['states'].message_type = _STATES
_COUNTRYMULTIPLERESPONSE.fields_by_name['country'].message_type = _COUNTRYREQUEST
_COUNTRYTABLERESPONSE.fields_by_name['items'].message_type = _COUNTRYREQUEST
DESCRIPTOR.message_types_by_name['CountryEmpty'] = _COUNTRYEMPTY
DESCRIPTOR.message_types_by_name['CitiesC'] = _CITIESC
DESCRIPTOR.message_types_by_name['States'] = _STATES
DESCRIPTOR.message_types_by_name['CountryRequest'] = _COUNTRYREQUEST
DESCRIPTOR.message_types_by_name['CountryTableRequest'] = _COUNTRYTABLEREQUEST
DESCRIPTOR.message_types_by_name['CountryMultipleResponse'] = _COUNTRYMULTIPLERESPONSE
DESCRIPTOR.message_types_by_name['CountryTableResponse'] = _COUNTRYTABLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CountryEmpty = _reflection.GeneratedProtocolMessageType('CountryEmpty', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYEMPTY,
  '__module__' : 'country_pb2'
  # @@protoc_insertion_point(class_scope:CountryEmpty)
  })
_sym_db.RegisterMessage(CountryEmpty)

CitiesC = _reflection.GeneratedProtocolMessageType('CitiesC', (_message.Message,), {
  'DESCRIPTOR' : _CITIESC,
  '__module__' : 'country_pb2'
  # @@protoc_insertion_point(class_scope:CitiesC)
  })
_sym_db.RegisterMessage(CitiesC)

States = _reflection.GeneratedProtocolMessageType('States', (_message.Message,), {
  'DESCRIPTOR' : _STATES,
  '__module__' : 'country_pb2'
  # @@protoc_insertion_point(class_scope:States)
  })
_sym_db.RegisterMessage(States)

CountryRequest = _reflection.GeneratedProtocolMessageType('CountryRequest', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYREQUEST,
  '__module__' : 'country_pb2'
  # @@protoc_insertion_point(class_scope:CountryRequest)
  })
_sym_db.RegisterMessage(CountryRequest)

CountryTableRequest = _reflection.GeneratedProtocolMessageType('CountryTableRequest', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYTABLEREQUEST,
  '__module__' : 'country_pb2'
  # @@protoc_insertion_point(class_scope:CountryTableRequest)
  })
_sym_db.RegisterMessage(CountryTableRequest)

CountryMultipleResponse = _reflection.GeneratedProtocolMessageType('CountryMultipleResponse', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYMULTIPLERESPONSE,
  '__module__' : 'country_pb2'
  # @@protoc_insertion_point(class_scope:CountryMultipleResponse)
  })
_sym_db.RegisterMessage(CountryMultipleResponse)

CountryTableResponse = _reflection.GeneratedProtocolMessageType('CountryTableResponse', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYTABLERESPONSE,
  '__module__' : 'country_pb2'
  # @@protoc_insertion_point(class_scope:CountryTableResponse)
  })
_sym_db.RegisterMessage(CountryTableResponse)



_COUNTRY = _descriptor.ServiceDescriptor(
  name='Country',
  full_name='Country',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=541,
  serialized_end=656,
  methods=[
  _descriptor.MethodDescriptor(
    name='table',
    full_name='Country.table',
    index=0,
    containing_service=None,
    input_type=_COUNTRYTABLEREQUEST,
    output_type=_COUNTRYTABLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_all',
    full_name='Country.get_all',
    index=1,
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
