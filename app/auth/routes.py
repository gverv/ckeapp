# app/auth/routes.py
from flask import render_template, redirect, url_for, flash, request    #, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash

from app import admin
from app.extensions import db
# from app.utils.permissions import role_required
from app.models.user import User
from .forms import LoginForm, RegisterForm
from . import auth_bp   # as auth




@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f"Επιτυχής σύνδεση", "success")

            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.index"))

        flash(f"Λάθος username ή password", "danger")

    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash(f"Αποσυνδεθήκατε", "info")
    # return redirect(url_for("auth_bp.login"))
    return redirect(url_for('main.index'))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash(f"Έχετε ήδη συνδεθεί {current_user.username}", "info")
        return redirect(url_for("main.index"))

    form = RegisterForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(
            username=form.username.data
        ).first()

        if existing_user:
            flash(f"Το username υπάρχει ήδη", "danger")
            return redirect(url_for("auth.register"))

        existing_email = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing_email:
            flash(f"Το email υπάρχει ήδη", "danger")
            return redirect(url_for("auth.register"))

        # 👉 Αν είναι ο ΠΡΩΤΟΣ χρήστης → admin
        is_first_user = User.query.count() == 0
        role = "admin" if is_first_user else "user"

        user = User(
            username = form.username.data,
            email = form.email.data,
            role = role
        )
        user.set_password(form.password.data)

        db.session.add(user)
        try:
            db.session.commit()    
        except Exception as e:
            flash(f"Σφάλμα κατά την εγγραφή {e}", category="danger")
            return redirect(url_for("main.index"))

        # ✅ Auto-login
        login_user(user)

        if role == "admin":
            flash(f"Δημιουργήθηκε ο πρώτος Διαχειριστής", "success")
        else:
            flash(f"Η εγγραφή για το χρήστη { user.username } ολοκληρώθηκε", "success")

        return redirect(url_for("main.index"))

    return render_template("auth/register.html", form=form)


#########################


@auth_bp.route("/admin-only")
@login_required
def admin_only():
    if current_user.role != "admin":
        flash(f"Δεν έχετε δικαίωμα πρόσβασης", "danger")
        return redirect(url_for("main.index"))

    return "Admin content"

# @admin.route("/dashboard")
# @login_required
# @role_required("admin")
# def dashboard():
#     return render_template("admin/dashboard.html")

@auth_bp.route('/reset-password')
def reset_password():
    return render_template('auth/reset_password.html')

@auth_bp.route('/profile')
def profile():
    return render_template('auth/profile.html')

@auth_bp.route('/change-password')
def change_password():
    return render_template('auth/change_password.html')

@auth_bp.route('/verify-email')
def verify_email():
    return render_template('auth/verify_email.html')

