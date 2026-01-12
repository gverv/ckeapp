# app/middleware.py

from flask import redirect, url_for, request
from flask_login import current_user
from app.models import AppSettings

def maintenance_middleware():
    settings = AppSettings.query.first()

    if not settings or not settings.maintenance_mode:
        return

    # Admin bypass
    if current_user.is_authenticated and current_user.is_admin():
        return

    # Allow login & static
    if request.endpoint in ("auth.login", "auth.logout", "static"):
        return

    return redirect(url_for("main.maintenance"))
