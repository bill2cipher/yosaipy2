from serializer import BaseSchema, MarshmallowSerializer, DictSchema
from marshmallow import fields, MarshalResult
from yosaipy2.web.session.schema import WebSimpleSession, WebSessionSchema


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
    under_type = User.__name__
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
ser.register_schema(WebSimpleSession, WebSessionSchema)
obj = User()

# result = ser.serialize(obj)  # type: MarshalResult
# print('###', result, type(result))
#
# result = ser.deserialize(result)
# print(result, type(result))
#
# result = ser.serialize(b)
# print('###', result, type(result))
#
# result = ser.deserialize(result)
# print(result, type(result))

session = WebSimpleSession("asdf", 1, 2, "sadf")
result = ser.serialize(session)
print('##', result, type(result))
result = ser.deserialize(result)
print('##', result, type(result))
