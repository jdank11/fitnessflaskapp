from flask import request
from uuid import uuid4
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask.views import MethodView
from flask_smorest import abort

from models.PostModel import PostModel
from . import bp as app

from schemas import PostSchema, PostSchemaNested


@app.route('/post/<post_id>')
class Post(MethodView):
  
  @app.response(200, PostSchemaNested)
  def get(self, post_id):
    post = PostModel.query.get(post_id)
    if post:
      print(post.posts.all())
      return post 
    abort(400, message='Invalid Post')

  @jwt_required()  
  @app.arguments(PostSchema)
  def put(self, post_data, post_id):
    post = PostModel.query.get(post_id)
    if post and post.user_id == get_jwt_identity():
      post.user_id = post_data['user_id']
      post.title = post_data['title']
      post.weight = post_data['weight']
      post.workout = post_data['workout']
      post.commit()
      return{ 'message': 'post updated'}, 201
    return {'message': "Invalid Post Id"}, 400
  
  @jwt_required()
  def delete(self, post_id):
    post = PostModel.query.get(post_id)
    if post and post.user_id == get_jwt_identity():
      post.delete()
      return {"message": "Post Deleted"}, 202
    return {'message':"Invalid Post"}, 400
    

@app.route('/post')
class PostList(MethodView):
  
  @app.response(200, PostSchema(many=True))
  def get(self):
    return PostModel.query.all()
  
  @jwt_required()
  @app.arguments(PostSchema)
  def post(self, post_data):
    try:
      post = PostModel()
      post.user_id = get_jwt_identity() 
      post.title = post_data['title']
      post.weight = post_data['weight']
      post.workout = post_data['workout']
      post.commit()
      return { 'message': "Post Created" }, 201
    except:
      return{'message' : "Invalid User"}, 401



# @app.get('/post')
# def get_posts():
#   return { 'posts': list(posts.values()) }

# @app.get('/post/<post_id>')
# def get_post(post_id):
#   try:
#     return {'post': posts[post_id]}, 200
#   except KeyError:
#     return {'message': "Invalid Post"}, 400

# @app.post('/post')
# def create_post():
#   user_id = post_data['user_id']
#   if user_id in users:
#     posts[uuid4()] = post_data
#     return { 'message': "Post Created" }, 201
#   return { 'message': "Invalid User"}, 401

# @app.put('/post/<post_id>')
# def update_post(post_id):
#   try:
#     post = posts[post_id]
#     post_data = request.get_json()
#     if post_data['user_id'] == post['user_id']:
#       post['title'] = post_data['title']
#       post['weight'] = post_data['weight']
#       post['workout'] = post_data['workout']
#       return { 'message': 'Post Updated' }, 202
#     return {'message': "Unauthorized"}, 401
#   except:
#     return {'message': "Invalid Post Id"}, 400

# @app.delete('/post/<post_id>')
# def delete_post(post_id):
#   try:
#     del posts[post_id]
#     return {"message": "Post Deleted"}, 202
#   except:
#     return {'message':"Invalid Post"}, 400