# app/utils/logs.py

from flask import request
from flask_login import current_user
from app.extensions import db
from app.models import ActivityLog


def log_action(action: str):
    """
    Καταγράφει ενέργεια χρήστη στο activity log
    """

    log = ActivityLog(
        user_id=current_user.id if current_user.is_authenticated else None,
        action=action,
        ip_address=request.remote_addr
    )

    db.session.add(log)
    try:
        db.session.commit()
    except Exception as e:
        print(f"Δεν καταγράφηκε στο activity_logs το:\n {log}")
