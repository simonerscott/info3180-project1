from . import db
from flask_sqlalchemy import SQLAlchemy


class UserProfile(db.Model):
    userid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80),unique = True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    age = db.Column(db.Integer())
    gender = db.Column(db.String(6))
    image = db.Column(db.String(80))
    bio = db.Column(db.Text)
    created_on = db.Column(db.DateTime)
    
    
    def __init__(self, userid, username, firstname, lastname, age, gender, image, bio, created_on):
        self.userid = userid
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.image = image
        self.bio = bio
        self.created_on = created_on

    def __repr__(self):
        return'<User %r>' % self.username

    # def is_authenticated(self):
    #     return True

    # def is_active(self):
    #     return True

    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     try:
    #         return unicode(self.userid)  # python 2 support
    #     except NameError:
    #         return str(self.userid)  # python 3 support
    
    
    
   