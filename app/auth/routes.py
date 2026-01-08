# app/auth/routes.py
from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash

from app import admin
from app.extensions import db
from app.utils.permissions import role_required
from app.models.user import User
from app.auth.forms import LoginForm
from . import auth


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Επιτυχής σύνδεση", "success")

            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.index"))

        flash("Λάθος username ή password", "danger")

    return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Αποσυνδεθήκατε", "info")
    # return redirect(url_for("auth.login"))
    return redirect(url_for('main.index'))

@auth.route("/admin-only")
@login_required
def admin_only():
    if current_user.role != "admin":
        flash("Δεν έχετε δικαίωμα πρόσβασης", "danger")
        return redirect(url_for("main.index"))

    return "Admin content"

# @admin.route("/dashboard")
# @login_required
# @role_required("admin")
# def dashboard():
#     return render_template("admin/dashboard.html")

@auth.route('/register')
def register():
    return render_template('auth/register.html')

@auth.route('/reset-password')
def reset_password():
    return render_template('auth/reset_password.html')

@auth.route('/profile')
def profile():
    return render_template('auth/profile.html')

@auth.route('/change-password')
def change_password():
    return render_template('auth/change_password.html')

@auth.route('/verify-email')
def verify_email():
    return render_template('auth/verify_email.html')

