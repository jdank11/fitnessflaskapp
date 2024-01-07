from marshmallow import Schema, fields

class UserSchema(Schema):
  id = fields.Str(dump_only = True)
  email = fields.Str(required = True)
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )
  first_name = fields.Str()
  last_name = fields.Str()

class PostSchema(Schema):
  id = fields.Str(dump_only = True)
  title = fields.Str(required = True)
  workout = fields.Str(required = True)
  weight = fields.Str(required = True)
  timestamp = fields.DateTime(dump_only = True)
  user_id = fields.Str(required = True)