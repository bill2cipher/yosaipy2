#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abcs import Serializer
from marshmallow import Schema, fields, post_load, pre_dump, post_dump


class DictWrapper(object):
    def __init__(self, data):
        self.data = data


class BaseSchema(Schema):
    schema_name = 'lSYx34'

    @post_dump
    def add_schema(self, data):
        data[self.schema_name] = self.__class__.__name__


class DictSchema(BaseSchema):
    data = fields.Dict()

    @pre_dump
    def encode(self, data):
        return DictWrapper(data)

    @post_load
    def decode(self, data):
        return data['data']


class MarshmallowSerializer(Serializer):
    def __init__(self):
        self._schemas = dict()

    def deserialize(self, data):
        schema_name = data[BaseSchema.schema_name]
        schema = self._schemas[schema_name]()
        return schema.load(data)

    def serialize(self, obj):
        schema = self._schemas[obj.__class__.__name__]()
        return schema.dump(obj)

    def register_schema(self, cls, schema):
        self._schemas[cls.__name__] = schema

    @property
    def mimetype(self):
        return 'application/marshallow'
