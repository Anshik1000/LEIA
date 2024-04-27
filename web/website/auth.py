from flask import Blueprint,render_template,request,redirect,url_for
from website.models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
auth = Blueprint('auth',__name__)




@auth.route('/quiz',methods=['GET','POST'])
def quiz():
    if(request.method=='POST'):
        username =request.form.get('username')
        password =request.form.get('password')
        learner=request.form.get('Learner')
        email=request.form.get('email')
        entry = User(UserName=username,Password=generate_password_hash(password,method='scrypt'),LearnerType=learner,Email=email)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template("quiz2.html")