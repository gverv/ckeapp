# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, Optional

class CreateUserForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=80)],
        render_kw={"class": "form-control"}
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"}
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=4)],
        render_kw={"class": "form-control"}
    )

    role = SelectField(
        "Role",
        choices=[
            ("user", "User"),
            ("admin", "Admin"),
        ],
        validators=[DataRequired()],
        render_kw={"class": "form-select"}
    )

    submit = SubmitField(
        "Δημιουργία",
        render_kw={"class": "btn btn-success"}
    )

class EditUserForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=80)],
        render_kw={"class": "form-control"}
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"}
    )

    role = SelectField(
        "Role",
        choices=[
            ("user", "User"),
            ("editor", "Editor"),
            ("admin", "Admin")
        ],
        validators=[DataRequired()],
        render_kw={"class": "form-select"}
    )

    password = PasswordField(
        "Νέος κωδικός (προαιρετικό)",
        validators=[Optional(), Length(min=4)],
        render_kw={"class": "form-control"}
    )

    submit = SubmitField(
        "Αποθήκευση",
        render_kw={"class": "btn btn-primary"}
    )

class AdminSettingsForm(FlaskForm):
    site_name = StringField(
        "Όνομα Ιστότοπου",
        validators=[DataRequired(), Length(max=100)],
        render_kw={"class": "form-control"}
    )

    maintenance_mode = BooleanField(
        "Maintenance mode",
        render_kw={"class": "form-check-input"}
    )

    allow_registration = BooleanField(
        "Επιτρέπεται εγγραφή χρηστών",
        render_kw={"class": "form-check-input"}
    )

    submit = SubmitField(
        "Αποθήκευση",
        render_kw={"class": "btn btn-primary"}
    )
