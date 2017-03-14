from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, IntegerField
from wtforms.validators import InputRequired



class NewUser(FlaskForm):
    firstname = StringField("First Name", validators = [InputRequired()])
    lastname = StringField("Last Name", validators = [InputRequired()])
    username = StringField("Username", validators = [InputRequired()])
    age = IntegerField("Age", validators = [InputRequired()])
    gender = RadioField('Gender', choices = [('Male','Male'),('Female','Female')])
    bio = TextAreaField("Biography", validators = [InputRequired()])