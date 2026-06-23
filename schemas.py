from marshmallow import fields, schema

class UserSchema(schema):
    id = fields.String()
    username = fields.String()
    email = fields.String()