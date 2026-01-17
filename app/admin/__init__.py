# app/admin/__init__.py

from flask import Blueprint, abort, request
from flask_login import current_user, login_required
from app.utils.decorators import admin_required
from app.utils.logs import log_action

admin_bp = Blueprint(
    "admin",
    __name__,
    template_folder="templates"
)

@admin_bp.before_request
def admin_auto_log():
    if not current_user.is_authenticated:
        return
    # Αγνόησε GET αν δεν θες noise
    if request.method == "GET":
        return
    action = f"ADMIN {request.method} {request.path}"
    log_action(action)

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
