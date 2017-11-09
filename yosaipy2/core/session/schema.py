#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import fields, post_load, pre_dump
from session import SimpleSession
from yosaipy2.core.serialize.serializer import BaseSchema
from yosaipy2.core.subject.schema import SimpleIdentifierSchema

class SimpleSessionSchema(BaseSchema):
    under_type = SimpleSession

    session_id = fields.String(allow_none=True)
    start_timestamp = fields.Integer(allow_none=True)
    stop_timestamp = fields.Integer(allow_none=True)
    last_access_time = fields.Integer(allow_none=True)
    idle_timeout = fields.Integer(allow_none=True)
    absolute_timeout = fields.Integer(allow_none=True)
    is_expired = fields.Boolean(allow_none=True)
    host = fields.String(allow_none=True)
    internal_attributes = fields.Dict(allow_none=True)
    attributes = fields.Dict(allow_none=True)

    @pre_dump
    def encode_attribute(self, data):
        internal_attributes = data['internal_attributes']
        if 'run_as_identifiers_session_key' in internal_attributes:
            pass
        elif 'authenticated_session_key' in internal_attributes:
            pass
        elif 'identifiers_session_key' in internal_attributes:
            pass

    @post_load
    def make_session(self, data):
        s = SimpleSession(data['absolute_timeout'], data['idle_timeout'], data['host'])
        for k in data:
            if hasattr(s, k):
                setattr(s, k, data[k])
        s.session_id = data['session_id']
        return s
