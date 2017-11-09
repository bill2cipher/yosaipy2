#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import fields, post_load
from session import WebSimpleSession
from yosaipy2.core.serialize.serializer import BaseSchema


class WebSessionSchema(BaseSchema):
    under_type = WebSimpleSession

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

    @post_load
    def make_session(self, data):
        csrf_token = data['internal_attributes']['csrf_token']
        s = WebSimpleSession(
            csrf_token=csrf_token,
            absolute_timeout=data['absolute_timeout'],
            idle_timeout=data['idle_timeout'],
            host=data['host']
        )
        s.session_id = data['session_id']
        s.start_timestamp = data['start_timestamp']
        s.stop_timestamp = data['stop_timestamp']
        s.last_access_time = data['last_access_time']
        s.idle_timeout = data['idle_timeout']
        s.absolute_timeout = data['absolute_timeout']
        s.is_expired = data['is_expired']
        s.host = data['host']
        s.attributes = data['attributes']
        s.internal_attributes = data['internal_attributes']
        return s
