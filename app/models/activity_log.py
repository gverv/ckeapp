# app/models/activity_log.py

from datetime import datetime, timezone
from app.extensions import db


class ActivityLog(db.Model):
    __tablename__ = "activity_logs"

    id = db.Column(db.Integer, primary_key=True)

    # ποιος έκανε την ενέργεια
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )

    # π.χ. "Delete user", "Login", "Create article"
    action = db.Column(db.String(150), nullable=False)

    # admin | auth | system | security
    category = db.Column(
        db.String(30),
        nullable=False,
        default="system",
        index=True
    )

    # optional στόχος (π.χ. user που διαγράφηκε)
    target_user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )

    # JSON extra info (ids, titles κλπ)
    extra = db.Column(db.Text, nullable=True)

    ip_address = db.Column(db.String(45), nullable=True)

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
        index=True
    )

    # relationships
    user = db.relationship(
        "User",
        foreign_keys=[user_id],
        backref="activity_logs"
    )

    target_user = db.relationship(
        "User",
        foreign_keys=[target_user_id]
    )

    def __repr__(self):
        return f"<ActivityLog {self.category}: {self.action}>"
