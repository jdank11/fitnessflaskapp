from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user_models import UserModel
from models.PostModel import PostModel

from resources.user import bp as user_bp
api.register_blueprint(user_bp)

from resources.post import bp as post_bp
api.register_blueprint(post_bp)