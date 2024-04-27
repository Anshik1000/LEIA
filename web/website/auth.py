from flask import Blueprint,render_template,request
from flask_sqlalchemy import SQLAlchemy
auth = Blueprint('auth',__name__)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    return render_template("signup.html")
