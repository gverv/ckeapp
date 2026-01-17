# app/models/user.py

from datetime import datetime, timezone
from flask_login import UserMixin
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "users"

    ROLE_ADMIN = "admin"
    ROLE_EDITOR = "editor"
    ROLE_USER = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(
        db.String(20),
        nullable=False,
        default=ROLE_USER
    )
    fullname = db.Column(db.String(50), nullable=True)
    fullname_genitive = db.Column(db.String(50), nullable=True)
    fullname_accusative = db.Column(db.String(50), nullable=True)
    fullname_vocative = db.Column(db.String(50), nullable=True)
    gender = db.Column(
        db.Enum("male", "female", name="gender_enum"),
        nullable=True
    )
    profile_image = db.Column(
        db.String(30),
        default="default_profile_image.jpg",
        nullable=False
    )
    date_created = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    articles = db.relationship("Article", back_populates="author", cascade="all, delete-orphan", lazy=True)

    def __repr__(self):
        return self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Helpers
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    def is_editor(self):
        return self.role == self.ROLE_EDITOR

    def is_user(self):
        return self.role == self.ROLE_USER
