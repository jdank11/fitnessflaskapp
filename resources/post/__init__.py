from flask_smorest import Blueprint

bp = Blueprint('posts', __name__, description="Operations for Posts")

from . import routes