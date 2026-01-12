# app/editor/__init__.py

from flask import Blueprint
from flask_login import login_required
from app.utils.permissions import editor_required

editor_bp = Blueprint(
    "editor",
    __name__,
    template_folder="templates"
)


@editor_bp.before_request
@login_required
@editor_required
def protect_editor():
    pass


