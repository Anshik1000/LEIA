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