# app/admin/routes.py

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.extensions import db
from app.models.user import User
from app.utils.permissions import admin_required
from . import admin_bp

@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route("/users")
def users():
    users = User.query.all()
    return render_template("admin/users/index.html", users=users)

@admin_bp.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
            role=request.form["role"]
        )
        user.set_password(request.form["password"])
        db.session.add(user)
        db.session.commit()
        flash("User created", "success")
        return redirect(url_for("admin.users"))

    return render_template("admin/users/create.html")

@admin_bp.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User {user.username} deleted", "warning")
    return redirect(url_for("admin.users"))


#########################

@admin_bp.route('/settings')
def settings():
    return render_template('admin/settings.html')

@admin_bp.route('/reports')
def reports():
    return render_template('admin/reports.html')

@admin_bp.route('/logs')
def logs():
    return render_template('admin/logs.html')

