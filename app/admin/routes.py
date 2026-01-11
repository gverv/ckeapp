# app/admin/routes.py
from flask import render_template
from flask_login import login_required
from . import admin_bp
from app.utils.permissions import admin_required


@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')


#########################

@admin_bp.route('/users')
def manage_users():
    return render_template('admin/manage_users.html')

@admin_bp.route('/settings')
def settings():
    return render_template('admin/settings.html')

@admin_bp.route('/reports')
def reports():
    return render_template('admin/reports.html')

@admin_bp.route('/logs')
def logs():
    return render_template('admin/logs.html')

