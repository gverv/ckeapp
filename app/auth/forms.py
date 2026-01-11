# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField
)
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField(
        "Όνομα χρήστη",
        validators=[DataRequired(), Length(min=3, max=80)],
        render_kw={"class": "form-control"}
    )

    password = PasswordField(
        "Κωδικός",
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )

    remember = BooleanField("Να με θυμάσαι")


    # email = EmailField(
    #     "Email",
    #     validators=[
    #         DataRequired(message="Το email είναι υποχρεωτικό"),
    #         Email
    #     ],
    #     render_kw={"class": "form-control", "placeholder": "Email"}
    # )

    submit = SubmitField(
        "Σύνδεση",
        render_kw={"class": "btn btn-primary w-100"}
    )


class RegisterForm(FlaskForm):
    username = StringField(
        "Όνομα χρήστη",
        validators=[DataRequired(), Length(min=3, max=80)],
        render_kw={"class": "form-control"}
    )

    password = PasswordField(
        "Κωδικός",
        validators=[DataRequired(), Length(min=4)],
        render_kw={"class": "form-control"}
    )

    confirm = PasswordField(
        "Επιβεβαίωση κωδικού",
        validators=[
            DataRequired(),
            EqualTo("password", message="Οι κωδικοί δεν ταιριάζουν")
        ],
        render_kw={"class": "form-control"}
    )

    submit = SubmitField(
        "Εγγραφή",
        render_kw={"class": "btn btn-success w-100"}
    )
