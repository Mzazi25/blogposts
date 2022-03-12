from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.widgets import TextArea


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
class BlogForm(FlaskForm):
   message = StringField('message', widget=TextArea(), validators=[InputRequired()])
   title = StringField('Blog Title',widget=TextArea(),validators=[InputRequired()])
class CommentForm(FlaskForm):
   comment = StringField('comment', widget=TextArea(), validators=[InputRequired()])
