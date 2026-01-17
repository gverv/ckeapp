# app/editor/__init__.py

from flask import Blueprint, abort, redirect, url_for
from flask_login import current_user

editor_bp = Blueprint(
    "editor",
    __name__,
    url_prefix="/editor",
    template_folder="templates"
)


@editor_bp.before_request
def protect_editor():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))

    if current_user.role not in ("editor", "admin"):
        abort(403)

from . import routes

