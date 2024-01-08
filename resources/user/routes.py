from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from . import bp as app
from db import users

from schemas import UserSchema
from models.user_models import UserModel

# user routes

@app.route('/user/<user_id>')
class User(MethodView):

  @app.response(200, UserSchema)  
  def get(self, user_id):
    user = UserModel.query.get(user_id)
    if user:
       return user
    else:
       abort(400, message= 'User not found')
  
  @app.arguments(UserSchema)
  def put(self, user_data, user_id):
    user = UserModel.query.get(user_id)
    if user: 
        user.from_dict(user_data)
        user.commit()
        return { 'message': f'{user.username} updated'}, 202
    abort(400, message= "Invalid User")
  
  def delete(self, user_id):
    user = UserModel.query.get(user_id)    
    if user:
        user.delete()
        return { 'message': f'User Deleted' }, 202
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

