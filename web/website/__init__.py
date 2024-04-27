from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='AKSJDHWUIAHSDKHJWIASHA'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/leia'
    db = SQLAlchemy(app)
    
    db.init_app(app)
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')


    return app

