from . import db
from flask_login import UserMixin


class User(db.Model,UserMixin):
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(20), nullable=False)
    LearnerType = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(20), nullable=False)

    def get_id(self):
        return (self.UserID)

class Turtle(db.Model):
    LevelID = db.Column(db.Integer, primary_key=True)
    LevelName = db.Column(db.String(50), nullable=False)

class Dolphin(db.Model):
    LevelID = db.Column(db.Integer, primary_key=True)
    LevelName = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.String(200))

class Elephant(db.Model):
    LevelID = db.Column(db.Integer, primary_key=True)
    LevelName = db.Column(db.String(50), nullable=False)

class Owl(db.Model):
    LevelID = db.Column(db.Integer, primary_key=True)
    LevelName = db.Column(db.String(50), nullable=False)

class Level(db.Model):
     UserID = db.Column(db.Integer,db.ForeignKey('User.UserID'), primary_key=True)
     LevelID = db.Column(db.Integer, primary_key=True)
     LevelName = db.Column(db.String(256), nullable=False)
     Progress = db.Column(db.Integer, nullable=False)
     