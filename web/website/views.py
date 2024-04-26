from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/quiz')
def quiz():
    return render_template("quiz2.html")

@views.route('/signup')
def signup():
    return render_template("signup.html")