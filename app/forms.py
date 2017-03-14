from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, IntegerField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired, FileField



class NewUser(FlaskForm):
    firstname = StringField("First Name", validators = [InputRequired()])
    lastname = StringField("Last Name", validators = [InputRequired()])
    username = StringField("Username", validators = [InputRequired()])
    age = IntegerField("Age", validators = [InputRequired()])
    gender = RadioField('Gender', choices = [('Male','Male'),('Female','Female'), ('Other','Other')])
    bio = TextAreaField("Biography", validators = [InputRequired()])
    img = FileField("Image", validators = [FileRequired()])