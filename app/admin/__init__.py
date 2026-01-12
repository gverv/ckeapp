# app/admin/__init__.py

from flask import Blueprint, abort
from flask_login import current_user, login_required
from app.utils.permissions import admin_required

admin_bp = Blueprint(
    "admin",
    __name__,
    template_folder="templates"
)

@admin_bp.before_request
@login_required
@admin_required
def protect_admin():
    pass
def restrict_to_admins():
    if not current_user.is_authenticated:
        abort(401)
    if not current_user.is_admin():
        abort(403)

from . import routes
