from flask_jwt_extended import create_access_token

from models.user_models import UserModel

from . import bp as app
from schemas import UserLogin

@app.post('/login')
@app.arguments(UserLogin)
def login(user_data):
  user = UserModel.query.filter_by(username = user_data['username']).first()
  if user and user.check_password(user_data['password']):
    access_token = create_access_token(user.id)
    return {'token': access_token}
  return {'message': 'Invalid user data'}