#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import Schema, fields, post_load
from session import SimpleSession


class SimpleSessionSchema(Schema):
    session_id = fields.String()
    start_timestamp = fields.Integer()
    stop_timestamp = fields.Integer()
    last_access_time = fields.Integer()
    idle_timeout = fields.Integer()
    absolute_timeout = fields.Integer()
    is_expired = fields.Boolean()
    host = fields.String()
    internal_attributes = fields.Dict()
    attributes = fields.Dict()

    @post_load
    def make_user(self, data):
        s = SimpleSession(data['absolute_timeout'], data['idle_timeout'], data['host'])
        for k in data:
            if hasattr(s, k):
                setattr(s, k, data[k])
        s.session_id = data['session_id']
