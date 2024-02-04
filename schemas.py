from marshmallow import Schema, fields

class UserSchema(Schema):
  id = fields.Str(dump_only = True)
  email = fields.Str(required = True)
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )
  first_name = fields.Str()
  last_name = fields.Str()
  token = fields.Str( dump_only = True )

class UserLogin(Schema):
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )
  
class PostSchema(Schema):
  id = fields.Str(dump_only = True)
  title = fields.Str(required = True)
  workout = fields.Str(required = True)
  weight = fields.Str(required = True)
  timestamp = fields.Str(dump_only = True)
  

class PostSchemaNested(PostSchema):
  user = fields.Nested(UserSchema, dump_only = True)

class UserSchemaNested(UserSchema):
  posts = fields.List(fields.Nested(PostSchema), dump_only=True)
  followed = fields.Function(lambda user: {followed.id: UserSchema().dump(followed) for followed in user.followed} )