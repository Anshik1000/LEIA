from flask import Blueprint,render_template,request,Flask,redirect,url_for,flash
import base64
from PIL import Image
from io import BytesIO
import os
from flask_login import  login_required,current_user
import numpy as np
import tensorflow as tf

views = Blueprint('views',__name__)
appli = Flask(__name__)
@views.route('/')
def home():
    if current_user.is_authenticated:
          return redirect(url_for('{}.home'.format(current_user.LearnerType.lower())))
    return render_template("index.html")

@views.route('/quiz')
def quiz():
    return render_template("quiz2.html")








@views.route('/home')
@login_required
def homepage():
    return render_template('learnerpath.html')
