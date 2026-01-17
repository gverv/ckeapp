# app/utils/logs.py

from flask import request, current_app
from flask_login import current_user
from app.extensions import db
from app.models.activity_log import ActivityLog
import json


def log_action(
    action: str,
    *,
    category: str = "system",
    target_user=None,
    extra: dict | None = None
):
    """
    Καταγράφει ενέργεια χρήστη στο activity log
    """
    log = ActivityLog(
        user_id=current_user.id if current_user.is_authenticated else None,
        action=action,
        category=category,
        target_user_id=target_user.id if target_user else None,
        ip_address=request.remote_addr,
        extra=json.dumps(extra) if extra else None
    )
    db.session.add(log)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(
            "Activity log failed",
            exc_info=e
        )

# Σχεδίαση decorator για log
def log_route(action):
    def decorator(f):
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            log_action(action)
            return result
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator

