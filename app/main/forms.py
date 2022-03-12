from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
