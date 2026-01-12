# app/models/settings.py

from app.extensions import db

class AppSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    site_name = db.Column(db.String(100), default="Flask App")
    maintenance_mode = db.Column(db.Boolean, default=False)
    allow_registration = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<AppSettings>"
