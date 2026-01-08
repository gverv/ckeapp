# app/utils/permissions.py
from functools import wraps
from flask import abort, redirect, url_for, flash
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not (current_user.is_authenticated and current_user.is_admin()):
            abort(403)
        return f(*args, **kwargs)
    return decorated

def editor_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not (current_user.is_authenticated and current_user.is_editor()):
            abort(403)
        return f(*args, **kwargs)
    return decorated

def viewer_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not (current_user.is_authenticated and current_user.is_viewer()):
            abort(403)
        return f(*args, **kwargs)
    return decorated

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for("auth.login"))
            if current_user.role not in roles:
                flash("Δεν έχετε δικαίωμα πρόσβασης", "danger")
                return redirect(url_for("main.index"))
            return f(*args, **kwargs)
        return wrapped
    return decorator

# Example usage:
# @app.route('/admin')
# @admin_required
# def admin_dashboard():
#     return "Welcome to the admin dashboard"
# @app.route('/edit')
# @editor_required
# def edit_page():
#     return "Welcome to the editor page"
# @app.route('/view')
# @viewer_required
# def view_page():
#     return "Welcome to the viewer page"
# @app.route('/special')
# @role_required('special_role')
# def special_page():
#     return "Welcome to the special role page"

# Note: The actual implementation of current_user methods like is_admin(), is_editor(), is_viewer(), and has_role()
# should be defined in the User model according to your application's requirements.
