from flask import request
from uuid import uuid4
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask.views import MethodView
from flask_smorest import abort

from . import bp as app


from schemas import UserSchema, UserSchemaNested
from models.user_models import UserModel


@app.route('/user/<user_id>')
class User(MethodView):

  @app.response(200, UserSchemaNested)  
  def get(self, user_id):
    user = UserModel.query.get(user_id)
    if user:
       print(user.posts.all())
       return user
    else:
       abort(400, message= 'User not found')
  
  @jwt_required()
  @app.arguments(UserSchema)
  def put(self, user_data, user_id):
    user = UserModel.query.get(get_jwt_identity())
    if user and user.id == int(user_id):
        user.from_dict(user_data)
        user.commit()
        return { 'message': f'User: {user.username} updated'}, 202
    abort(400, message= "Invalid User")
  
  @jwt_required()
  def delete(self, user_id):
    user = UserModel.query.get(get_jwt_identity())   
    if user and user.id == int(user_id):
        user.delete()
        return { 'message': f'User: {user.username} Deleted'  }, 202
    abort(400, message= "Invalid Username")



@app.route('/user')
class UserList(MethodView):
   
   @app.response(200, UserSchema(many=True))
   def get(self):
      return UserModel.query.all()
   
   @app.arguments(UserSchema)
   def post(self, user_data):
    try:
      user = UserModel()
      user.from_dict(user_data)
      user.commit()
      return { 'message' : f'{user_data["username"]} created' }, 201
    except:
       abort(400, message= "Username and Email already taken")

@app.route('/user/follow/<followed_id>')
class FollowUser(MethodView):

  @jwt_required()
  def post(self, followed_id):
    followed = UserModel.query.get(followed_id)
    follower = UserModel.query.get(get_jwt_identity())
    if follower and followed:
      follower.follow(followed)
      followed.commit()
      return {'message':'User Followed'}
    else:
      return {'message':'Invalid User'}, 400
      
  @jwt_required()  
  def put(self, followed_id):
    followed = UserModel.query.get(followed_id)
    follower = UserModel.query.get(get_jwt_identity())
    if follower and followed:
      follower.unfollow(followed)
      followed.commit()
      return {'message':'User Unfollowed'}
    else:
      return {'message':'Invalid User'}, 400


# @app.response(200, UserSchema(many=True))
# @app.get('/user')
# def user():
#   return { 'users': list(users.values()) }, 200

# @app.post('/user')
# @app.arguments(UserSchema)
# def create_user(user_data):
#   users[uuid4()] = user_data
#   return { 'message' : f'{user_data["username"]} created' }, 201



# @app.get('/user/<user_id>')
# @app.response(200, UserSchema)
# def get_user(user_id):
#   try:
#     return { 'user': users[user_id] } 
#   except:
#     return {'message': 'invalid user'}, 400

# @app.put('/user/<user_id>')
# def update_user(user_id):
#   try:
#     user = users[user_id]
#     user_data = request.get_json()
#     user |= user_data
#     return { 'message': f'{user["username"]} updated'}, 202
#   except KeyError:
#     return {'message': "Invalid User"}, 400
      
# @app.delete('/user/<user_id>')
# def delete_user(user_id):
#   try:
#     del users[user_id]
#     return { 'message': f'User Deleted' }, 202
#   except:
#     return {'message': "Invalid username"}, 400

