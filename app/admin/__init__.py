# app/admin/__init__.py
from flask import Blueprint
admin_bp = Blueprint('admin', __name__, template_folder='templates', static_folder='static')
# from . import views  # Import views to register routes
# from . import models  # Import models to register admin models