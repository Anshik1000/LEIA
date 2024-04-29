from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/quiz')
def quiz():
    return render_template("quiz2.html")

@views.route('/game')
def game():
    return render_template('recognition.html')

@views.route('/home')
def homepage():
    return render_template('learnerpath.html')