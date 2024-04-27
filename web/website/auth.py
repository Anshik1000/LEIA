from flask import Blueprint,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
auth = Blueprint('auth',__name__)


