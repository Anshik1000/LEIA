from flask import Blueprint,render_template,request,redirect,url_for,flash
from website.models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user,current_user
auth = Blueprint('auth',__name__)




@auth.route('/quiz',methods=['GET','POST'])
def quiz():
    if(request.method=='POST'):
        username =request.form.get('username')
        password =request.form.get('password')
        confirm_password = request.form.get('password2')
        learner=request.form.get('Learner')
        email=request.form.get('email')
        user = User.query.filter_by(Email=email).first()
        if user:
           flash("email already exists!")
        elif password!= confirm_password:
            flash("Passwords do not match!",category='error')
        else:
            entry = User(UserName=username,Password=generate_password_hash(password,method='scrypt'),LearnerType=learner,Email=email)
            db.session.add(entry)
            db.session.commit()
            user = User.query.filter_by(Email=email).first()
            login_user(user,remember=True) #creates session for the user
            flash('Account created',category='success')
            return redirect(url_for('views.homepage'))

        
    return render_template("quiz2.html")
@auth.route('/login',methods=['POST','GET'])
def login():
     if(request.method=='POST'):
         email=request.form.get('email')
         password = request.form.get('password')

         user = User.query.filter_by(Email=email).first()
         if user:
             if check_password_hash(user.Password,password):
                 login_user(user,remember=True)#creates session for the user
                 return redirect(url_for('views.homepage'))
             else:
                flash("Incorrect password,try again",category='error')
         else:
          flash("Email does not exist.",category='error')
        

     return render_template('login2.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))