# app/auth/__init__.py
from flask import Blueprint
from app.auth.routes import auth

auth_bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')
# auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

from . import routes
