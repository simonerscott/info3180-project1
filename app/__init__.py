from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# Config Values
# location where file uploads will be stored
UPLOAD_FOLDER = './app/static/uploads'



app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)
app.config.from_object(__name__)
from app import views