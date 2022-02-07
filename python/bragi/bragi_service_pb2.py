# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bragi/bragi_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from bragi_schema.bragi import csgo_pb2 as bragi_dot_csgo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bragi/bragi_service.proto',
  package='bragi',
  syntax='proto3',
  serialized_options=b'\n\017com.oddin.bragiZ\016oddin.gg/bragi',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x62ragi/bragi_service.proto\x12\x05\x62ragi\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x10\x62ragi/csgo.proto\"O\n\x13LiveDataFeedRequest\x12.\n\x05\x61\x66ter\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x42\x08\n\x06_after\"m\n\x13LiveDataFeedMessage\x12%\n\tkeepalive\x18\x01 \x01(\x0b\x32\x10.bragi.KeepAliveH\x00\x12$\n\x05match\x18\x02 \x01(\x0b\x32\x13.bragi.MatchMessageH\x00\x42\t\n\x07message\":\n\tKeepAlive\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9f\x01\n\x0cMatchMessage\x12(\n\x08snapshot\x18\x01 \x01(\x0b\x32\x14.bragi.MatchSnapshotH\x00\x12\x31\n\x0c\x61nnouncement\x18\x02 \x01(\x0b\x32\x19.bragi.AnnouncementUpdateH\x00\x12\'\n\x04\x63sgo\x18\x03 \x01(\x0b\x32\x17.bragi.CsgoMatchMessageH\x00\x42\t\n\x07message\"\x8b\x02\n\rMatchSnapshot\x12\x11\n\tmatch_urn\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\rannouncements\x18\x04 \x03(\x0b\x32\x13.bragi.Announcement\x12\x38\n\x0bmatch_state\x18\x05 \x01(\x0b\x32#.bragi.MatchSnapshot.GameMatchState\x1a@\n\x0eGameMatchState\x12%\n\x04\x63sgo\x18\x01 \x01(\x0b\x32\x15.bragi.CsgoMatchStateH\x00\x42\x07\n\x05state\"\x8e\x01\n\x12\x41nnouncementUpdate\x12\x11\n\tmatch_urn\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\x07payload\x18\x04 \x01(\x0b\x32\x13.bragi.Announcement\"\xe3\x01\n\x0c\x41nnouncement\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x07payload\x18\x02 \x01(\x0b\x32\x1b.bragi.Announcement.Payload\x1au\n\x07Payload\x12-\n\x07\x63ontrol\x18\x01 \x01(\x0b\x32\x1a.bragi.ControlAnnouncementH\x00\x12\x30\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1f.bragi.ControlErrorAnnouncementH\x00\x42\t\n\x07payload\"\xbf\x01\n\x13\x43ontrolAnnouncement\x12@\n\x04type\x18\x01 \x01(\x0e\x32\x32.bragi.ControlAnnouncement.ControlAnnouncementType\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\"D\n\x17\x43ontrolAnnouncementType\x12)\n%CONTROL_ANNOUNCEMENT_TYPE_UNSPECIFIED\x10\x00\x42\n\n\x08_message\"\xd9\x01\n\x18\x43ontrolErrorAnnouncement\x12J\n\x04type\x18\x01 \x01(\x0e\x32<.bragi.ControlErrorAnnouncement.ControlErrorAnnouncementType\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\"O\n\x1c\x43ontrolErrorAnnouncementType\x12/\n+CONTROL_ERROR_ANNOUNCEMENT_TYPE_UNSPECIFIED\x10\x00\x42\n\n\x08_message2S\n\x05\x42ragi\x12J\n\x0cLiveDataFeed\x12\x1a.bragi.LiveDataFeedRequest\x1a\x1a.bragi.LiveDataFeedMessage\"\x00\x30\x01\x42!\n\x0f\x63om.oddin.bragiZ\x0eoddin.gg/bragib\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,bragi_dot_csgo__pb2.DESCRIPTOR,])



_CONTROLANNOUNCEMENT_CONTROLANNOUNCEMENTTYPE = _descriptor.EnumDescriptor(
  name='ControlAnnouncementType',
  full_name='bragi.ControlAnnouncement.ControlAnnouncementType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTROL_ANNOUNCEMENT_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1258,
  serialized_end=1326,
)
_sym_db.RegisterEnumDescriptor(_CONTROLANNOUNCEMENT_CONTROLANNOUNCEMENTTYPE)

_CONTROLERRORANNOUNCEMENT_CONTROLERRORANNOUNCEMENTTYPE = _descriptor.EnumDescriptor(
  name='ControlErrorAnnouncementType',
  full_name='bragi.ControlErrorAnnouncement.ControlErrorAnnouncementType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTROL_ERROR_ANNOUNCEMENT_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1467,
  serialized_end=1546,
)
_sym_db.RegisterEnumDescriptor(_CONTROLERRORANNOUNCEMENT_CONTROLERRORANNOUNCEMENTTYPE)


_LIVEDATAFEEDREQUEST = _descriptor.Descriptor(
  name='LiveDataFeedRequest',
  full_name='bragi.LiveDataFeedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='after', full_name='bragi.LiveDataFeedRequest.after', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_after', full_name='bragi.LiveDataFeedRequest._after',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=87,
  serialized_end=166,
)


_LIVEDATAFEEDMESSAGE = _descriptor.Descriptor(
  name='LiveDataFeedMessage',
  full_name='bragi.LiveDataFeedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keepalive', full_name='bragi.LiveDataFeedMessage.keepalive', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='match', full_name='bragi.LiveDataFeedMessage.match', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='bragi.LiveDataFeedMessage.message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=168,
  serialized_end=277,
)


_KEEPALIVE = _descriptor.Descriptor(
  name='KeepAlive',
  full_name='bragi.KeepAlive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='bragi.KeepAlive.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=279,
  serialized_end=337,
)


_MATCHMESSAGE = _descriptor.Descriptor(
  name='MatchMessage',
  full_name='bragi.MatchMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot', full_name='bragi.MatchMessage.snapshot', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='announcement', full_name='bragi.MatchMessage.announcement', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='csgo', full_name='bragi.MatchMessage.csgo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='bragi.MatchMessage.message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=340,
  serialized_end=499,
)


_MATCHSNAPSHOT_GAMEMATCHSTATE = _descriptor.Descriptor(
  name='GameMatchState',
  full_name='bragi.MatchSnapshot.GameMatchState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='csgo', full_name='bragi.MatchSnapshot.GameMatchState.csgo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='state', full_name='bragi.MatchSnapshot.GameMatchState.state',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=705,
  serialized_end=769,
)

_MATCHSNAPSHOT = _descriptor.Descriptor(
  name='MatchSnapshot',
  full_name='bragi.MatchSnapshot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='match_urn', full_name='bragi.MatchSnapshot.match_urn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='bragi.MatchSnapshot.sequence', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='bragi.MatchSnapshot.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='announcements', full_name='bragi.MatchSnapshot.announcements', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='match_state', full_name='bragi.MatchSnapshot.match_state', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MATCHSNAPSHOT_GAMEMATCHSTATE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=769,
)


_ANNOUNCEMENTUPDATE = _descriptor.Descriptor(
  name='AnnouncementUpdate',
  full_name='bragi.AnnouncementUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='match_urn', full_name='bragi.AnnouncementUpdate.match_urn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='bragi.AnnouncementUpdate.sequence', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='bragi.AnnouncementUpdate.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='bragi.AnnouncementUpdate.payload', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=772,
  serialized_end=914,
)


_ANNOUNCEMENT_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='bragi.Announcement.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='control', full_name='bragi.Announcement.Payload.control', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='bragi.Announcement.Payload.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='bragi.Announcement.Payload.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1027,
  serialized_end=1144,
)

_ANNOUNCEMENT = _descriptor.Descriptor(
  name='Announcement',
  full_name='bragi.Announcement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='created_at', full_name='bragi.Announcement.created_at', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='bragi.Announcement.payload', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ANNOUNCEMENT_PAYLOAD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=917,
  serialized_end=1144,
)


_CONTROLANNOUNCEMENT = _descriptor.Descriptor(
  name='ControlAnnouncement',
  full_name='bragi.ControlAnnouncement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='bragi.ControlAnnouncement.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='bragi.ControlAnnouncement.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTROLANNOUNCEMENT_CONTROLANNOUNCEMENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_message', full_name='bragi.ControlAnnouncement._message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1147,
  serialized_end=1338,
)


_CONTROLERRORANNOUNCEMENT = _descriptor.Descriptor(
  name='ControlErrorAnnouncement',
  full_name='bragi.ControlErrorAnnouncement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='bragi.ControlErrorAnnouncement.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='bragi.ControlErrorAnnouncement.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTROLERRORANNOUNCEMENT_CONTROLERRORANNOUNCEMENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_message', full_name='bragi.ControlErrorAnnouncement._message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1341,
  serialized_end=1558,
)

_LIVEDATAFEEDREQUEST.fields_by_name['after'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LIVEDATAFEEDREQUEST.oneofs_by_name['_after'].fields.append(
  _LIVEDATAFEEDREQUEST.fields_by_name['after'])
_LIVEDATAFEEDREQUEST.fields_by_name['after'].containing_oneof = _LIVEDATAFEEDREQUEST.oneofs_by_name['_after']
_LIVEDATAFEEDMESSAGE.fields_by_name['keepalive'].message_type = _KEEPALIVE
_LIVEDATAFEEDMESSAGE.fields_by_name['match'].message_type = _MATCHMESSAGE
_LIVEDATAFEEDMESSAGE.oneofs_by_name['message'].fields.append(
  _LIVEDATAFEEDMESSAGE.fields_by_name['keepalive'])
_LIVEDATAFEEDMESSAGE.fields_by_name['keepalive'].containing_oneof = _LIVEDATAFEEDMESSAGE.oneofs_by_name['message']
_LIVEDATAFEEDMESSAGE.oneofs_by_name['message'].fields.append(
  _LIVEDATAFEEDMESSAGE.fields_by_name['match'])
_LIVEDATAFEEDMESSAGE.fields_by_name['match'].containing_oneof = _LIVEDATAFEEDMESSAGE.oneofs_by_name['message']
_KEEPALIVE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MATCHMESSAGE.fields_by_name['snapshot'].message_type = _MATCHSNAPSHOT
_MATCHMESSAGE.fields_by_name['announcement'].message_type = _ANNOUNCEMENTUPDATE
_MATCHMESSAGE.fields_by_name['csgo'].message_type = bragi_dot_csgo__pb2._CSGOMATCHMESSAGE
_MATCHMESSAGE.oneofs_by_name['message'].fields.append(
  _MATCHMESSAGE.fields_by_name['snapshot'])
_MATCHMESSAGE.fields_by_name['snapshot'].containing_oneof = _MATCHMESSAGE.oneofs_by_name['message']
_MATCHMESSAGE.oneofs_by_name['message'].fields.append(
  _MATCHMESSAGE.fields_by_name['announcement'])
_MATCHMESSAGE.fields_by_name['announcement'].containing_oneof = _MATCHMESSAGE.oneofs_by_name['message']
_MATCHMESSAGE.oneofs_by_name['message'].fields.append(
  _MATCHMESSAGE.fields_by_name['csgo'])
_MATCHMESSAGE.fields_by_name['csgo'].containing_oneof = _MATCHMESSAGE.oneofs_by_name['message']
_MATCHSNAPSHOT_GAMEMATCHSTATE.fields_by_name['csgo'].message_type = bragi_dot_csgo__pb2._CSGOMATCHSTATE
_MATCHSNAPSHOT_GAMEMATCHSTATE.containing_type = _MATCHSNAPSHOT
_MATCHSNAPSHOT_GAMEMATCHSTATE.oneofs_by_name['state'].fields.append(
  _MATCHSNAPSHOT_GAMEMATCHSTATE.fields_by_name['csgo'])
_MATCHSNAPSHOT_GAMEMATCHSTATE.fields_by_name['csgo'].containing_oneof = _MATCHSNAPSHOT_GAMEMATCHSTATE.oneofs_by_name['state']
_MATCHSNAPSHOT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MATCHSNAPSHOT.fields_by_name['announcements'].message_type = _ANNOUNCEMENT
_MATCHSNAPSHOT.fields_by_name['match_state'].message_type = _MATCHSNAPSHOT_GAMEMATCHSTATE
_ANNOUNCEMENTUPDATE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ANNOUNCEMENTUPDATE.fields_by_name['payload'].message_type = _ANNOUNCEMENT
_ANNOUNCEMENT_PAYLOAD.fields_by_name['control'].message_type = _CONTROLANNOUNCEMENT
_ANNOUNCEMENT_PAYLOAD.fields_by_name['error'].message_type = _CONTROLERRORANNOUNCEMENT
_ANNOUNCEMENT_PAYLOAD.containing_type = _ANNOUNCEMENT
_ANNOUNCEMENT_PAYLOAD.oneofs_by_name['payload'].fields.append(
  _ANNOUNCEMENT_PAYLOAD.fields_by_name['control'])
_ANNOUNCEMENT_PAYLOAD.fields_by_name['control'].containing_oneof = _ANNOUNCEMENT_PAYLOAD.oneofs_by_name['payload']
_ANNOUNCEMENT_PAYLOAD.oneofs_by_name['payload'].fields.append(
  _ANNOUNCEMENT_PAYLOAD.fields_by_name['error'])
_ANNOUNCEMENT_PAYLOAD.fields_by_name['error'].containing_oneof = _ANNOUNCEMENT_PAYLOAD.oneofs_by_name['payload']
_ANNOUNCEMENT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ANNOUNCEMENT.fields_by_name['payload'].message_type = _ANNOUNCEMENT_PAYLOAD
_CONTROLANNOUNCEMENT.fields_by_name['type'].enum_type = _CONTROLANNOUNCEMENT_CONTROLANNOUNCEMENTTYPE
_CONTROLANNOUNCEMENT_CONTROLANNOUNCEMENTTYPE.containing_type = _CONTROLANNOUNCEMENT
_CONTROLANNOUNCEMENT.oneofs_by_name['_message'].fields.append(
  _CONTROLANNOUNCEMENT.fields_by_name['message'])
_CONTROLANNOUNCEMENT.fields_by_name['message'].containing_oneof = _CONTROLANNOUNCEMENT.oneofs_by_name['_message']
_CONTROLERRORANNOUNCEMENT.fields_by_name['type'].enum_type = _CONTROLERRORANNOUNCEMENT_CONTROLERRORANNOUNCEMENTTYPE
_CONTROLERRORANNOUNCEMENT_CONTROLERRORANNOUNCEMENTTYPE.containing_type = _CONTROLERRORANNOUNCEMENT
_CONTROLERRORANNOUNCEMENT.oneofs_by_name['_message'].fields.append(
  _CONTROLERRORANNOUNCEMENT.fields_by_name['message'])
_CONTROLERRORANNOUNCEMENT.fields_by_name['message'].containing_oneof = _CONTROLERRORANNOUNCEMENT.oneofs_by_name['_message']
DESCRIPTOR.message_types_by_name['LiveDataFeedRequest'] = _LIVEDATAFEEDREQUEST
DESCRIPTOR.message_types_by_name['LiveDataFeedMessage'] = _LIVEDATAFEEDMESSAGE
DESCRIPTOR.message_types_by_name['KeepAlive'] = _KEEPALIVE
DESCRIPTOR.message_types_by_name['MatchMessage'] = _MATCHMESSAGE
DESCRIPTOR.message_types_by_name['MatchSnapshot'] = _MATCHSNAPSHOT
DESCRIPTOR.message_types_by_name['AnnouncementUpdate'] = _ANNOUNCEMENTUPDATE
DESCRIPTOR.message_types_by_name['Announcement'] = _ANNOUNCEMENT
DESCRIPTOR.message_types_by_name['ControlAnnouncement'] = _CONTROLANNOUNCEMENT
DESCRIPTOR.message_types_by_name['ControlErrorAnnouncement'] = _CONTROLERRORANNOUNCEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LiveDataFeedRequest = _reflection.GeneratedProtocolMessageType('LiveDataFeedRequest', (_message.Message,), {
  'DESCRIPTOR' : _LIVEDATAFEEDREQUEST,
  '__module__' : 'bragi.bragi_service_pb2'
  # @@protoc_insertion_point(class_scope:bragi.LiveDataFeedRequest)
  })
_sym_db.RegisterMessage(LiveDataFeedRequest)

LiveDataFeedMessage = _reflection.GeneratedProtocolMessageType('LiveDataFeedMessage', (_message.Message,), {
  'DESCRIPTOR' : _LIVEDATAFEEDMESSAGE,
  '__module__' : 'bragi.bragi_service_pb2'
  # @@protoc_insertion_point(class_scope:bragi.LiveDataFeedMessage)
  })
_sym_db.RegisterMessage(LiveDataFeedMessage)

KeepAlive = _reflection.GeneratedProtocolMessageType('KeepAlive', (_message.Message,), {
  'DESCRIPTOR' : _KEEPALIVE,
  '__module__' : 'bragi.bragi_service_pb2'
  # @@protoc_insertion_point(class_scope:bragi.KeepAlive)
  })
_sym_db.RegisterMessage(KeepAlive)

MatchMessage = _reflection.GeneratedProtocolMessageType('MatchMessage', (_message.Message,), {
  'DESCRIPTOR' : _MATCHMESSAGE,
  '__module__' : 'bragi.bragi_service_pb2'
  # @@protoc_insertion_point(class_scope:bragi.MatchMessage)
  })
_sym_db.RegisterMessage(MatchMessage)

MatchSnapshot = _reflection.GeneratedProtocolMessageType('MatchSnapshot', (_message.Message,), {

  'GameMatchState' : _reflection.GeneratedProtocolMessageType('GameMatchState', (_message.Message,), {
    'DESCRIPTOR' : _MATCHSNAPSHOT_GAMEMATCHSTATE,
    '__module__' : 'bragi.bragi_service_pb2'
    # @@protoc_insertion_point(class_scope:bragi.MatchSnapshot.GameMatchState)
    })
  ,
  'DESCRIPTOR' : _MATCHSNAPSHOT,
  '__module__' : 'bragi.bragi_service_pb2'
  # @@protoc_insertion_point(class_scope:bragi.MatchSnapshot)
  })
_sym_db.RegisterMessage(MatchSnapshot)
_sym_db.RegisterMessage(MatchSnapshot.GameMatchState)

AnnouncementUpdate = _reflection.GeneratedProtocolMessageType('AnnouncementUpdate', (_message.Message,), {
  'DESCRIPTOR' : _ANNOUNCEMENTUPDATE,
  '__module__' : 'bragi.bragi_service_pb2'
  # @@protoc_insertion_point(class_scope:bragi.AnnouncementUpdate)
  })
_sym_db.RegisterMessage(AnnouncementUpdate)

Announcement = _reflection.GeneratedProtocolMessageType('Announcement', (_message.Message,), {

  'Payload' : _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), {
    'DESCRIPTOR' : _ANNOUNCEMENT_PAYLOAD,
    '__module__' : 'bragi.bragi_service_pb2'
    # @@protoc_insertion_point(class_scope:bragi.Announcement.Payload)
    })
  ,
  'DESCRIPTOR' : _ANNOUNCEMENT,
  '__module__' : 'bragi.bragi_service_pb2'
  # @@protoc_insertion_point(class_scope:bragi.Announcement)
  })
_sym_db.RegisterMessage(Announcement)
_sym_db.RegisterMessage(Announcement.Payload)

ControlAnnouncement = _reflection.GeneratedProtocolMessageType('ControlAnnouncement', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLANNOUNCEMENT,
  '__module__' : 'bragi.bragi_service_pb2'
  # @@protoc_insertion_point(class_scope:bragi.ControlAnnouncement)
  })
_sym_db.RegisterMessage(ControlAnnouncement)

ControlErrorAnnouncement = _reflection.GeneratedProtocolMessageType('ControlErrorAnnouncement', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLERRORANNOUNCEMENT,
  '__module__' : 'bragi.bragi_service_pb2'
  # @@protoc_insertion_point(class_scope:bragi.ControlErrorAnnouncement)
  })
_sym_db.RegisterMessage(ControlErrorAnnouncement)


DESCRIPTOR._options = None

_BRAGI = _descriptor.ServiceDescriptor(
  name='Bragi',
  full_name='bragi.Bragi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1560,
  serialized_end=1643,
  methods=[
  _descriptor.MethodDescriptor(
    name='LiveDataFeed',
    full_name='bragi.Bragi.LiveDataFeed',
    index=0,
    containing_service=None,
    input_type=_LIVEDATAFEEDREQUEST,
    output_type=_LIVEDATAFEEDMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BRAGI)

DESCRIPTOR.services_by_name['Bragi'] = _BRAGI

# @@protoc_insertion_point(module_scope)
