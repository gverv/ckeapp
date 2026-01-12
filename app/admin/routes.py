# app/admin/routes.py

from flask import render_template, redirect, url_for, flash #, request
# from flask_login import login_required
from app.extensions import db
# from app.utils.permissions import admin_required
from app.models import AppSettings, User, Post
from .forms import AdminSettingsForm, EditUserForm, CreateUserForm
from . import admin_bp

@admin_bp.route("/settings", methods=["GET", "POST"])
def settings():
    settings = AppSettings.query.first()
    if not settings:
        settings = AppSettings()
        db.session.add(settings)
        try:
            db.session.commit()
        except Exception as e:
            flash(f"Σφάλμα κατά την εγγραφή των ρυθμίσεων στη βάση δεδομένων {e}")
    form = AdminSettingsForm(obj=settings)
    if form.validate_on_submit():
        settings.site_name = form.site_name.data
        settings.maintenance_mode = form.maintenance_mode.data
        settings.allow_registration = form.allow_registration.data
        try:
            db.session.commit()
        except Exception as e:
            flash(f"Σφάλμα κατά την εγγραφή των ρυθμίσεων στη βάση δεδομένων {e}")
        flash(f"Οι ρυθμίσεις αποθηκεύτηκαν", "success")
        return redirect(url_for("admin.settings"))
    return render_template("admin/settings.html", form=form)


@admin_bp.route('/')
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route("/users")
def users():
    users = User.query.order_by(User.id).all()
    return render_template("admin/users/index.html", users=users)

@admin_bp.route("/users/create", methods=["GET", "POST"])
def create_user():
    form = CreateUserForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            role=form.role.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            flash(f"Σφάλμα κατά την εγγραφή του χρήστη. {e}", "danger")
        flash(f"Ο χρήστης { user.username } δημιουργήθηκε!", "success")
        return redirect(url_for("admin.users"))

    return render_template("admin/users/create.html")

@admin_bp.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f"Ο χρήστης {user.username} διαγράφηκε", "warning")
    return redirect(url_for("admin.users"))

@admin_bp.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = EditUserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.role = form.role.data
        if form.password.data:
            user.set_password(form.password.data)
        try:
            db.session.commit()
        except Exception as e:
            flash(f"Σφάλμα εγγραφής αλλαγών στη βάση {e}\nγια το χρήστη {user.username}.", category="danger")
            return redirect(url_for("admin.users"))
        flash(f"Ο χρήστης {user.username} ενημερώθηκε.", category="success")
        return redirect(url_for("admin.users"))

    return render_template("admin/users/edit.html", form=form, user=user)
#########################

@admin_bp.route('/reports')
def reports():
    return render_template('admin/reports.html')

@admin_bp.route('/logs')
def logs():
    return render_template('admin/logs.html')

