from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    
    username = StringField(
        "Όνομα χρήστη",
        validators=[
            DataRequired(message="Το username είναι υποχρεωτικό"),
            Length(min=3, max=80)
        ],
        render_kw={"class": "form-control", "placeholder": "Username"}
    )

    # email = EmailField(
    #     "Email",
    #     validators=[
    #         DataRequired(message="Το email είναι υποχρεωτικό"),
    #         Email
    #     ],
    #     render_kw={"class": "form-control", "placeholder": "Email"}
    # )

    password = PasswordField(
        "Κωδικός",
        validators=[
            DataRequired(message="Το password είναι υποχρεωτικό"),
            Length(min=4)
        ],
        render_kw={"class": "form-control", "placeholder": "Password"}
    )

    remember = BooleanField(
        "Να με θυμάσαι",
        render_kw={"class": "form-check-input"}
    )

    submit = SubmitField(
        "Σύνδεση",
        render_kw={"class": "btn btn-primary w-100"}
    )
