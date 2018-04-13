from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, PasswordField
from wtforms.validators import InputRequired, DataRequired, Email

class UploadForm(FlaskForm):
    description = TextAreaField('Description')
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])