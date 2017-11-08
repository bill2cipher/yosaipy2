from serializer import BaseSchema, MarshmallowSerializer, DictSchema
from marshmallow import fields, MarshalResult


class User:
    def __init__(self):
        self.name = "asdf"
        self.password = "password"
        self.good = {
            "good": 1,
            "bad": 2,
            "think": "right"
        }


class UserSchema(BaseSchema):
    name = fields.String()
    password = fields.String()
    good = fields.Dict()

b = {
    'home': 12,
    "remove": "think",
    "bad": {
        "good": "ok",
        "really": 55
    }
}

ser = MarshmallowSerializer()
ser.register_schema(User, UserSchema)
ser.register_schema(dict, DictSchema)
obj = User()

result = ser.serialize(obj)  # type: MarshalResult
print('###', result, type(result))


result = ser.serialize(b)
print('###', result, type(result))