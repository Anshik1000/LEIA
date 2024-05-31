from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='AKSJDHWUIAHSDKHJWIASHA'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/leia'
   
    
    db.init_app(app)
    from .models import User
    login_manager = LoginManager()
    #where should flask redirect if user is not logged in
    login_manager.login_view = 'views.home'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(UserID):
        return User.query.get(int(UserID))
  
    from .views import views
    from .auth import auth
    from .turtle import turtle
    from .dolphin import dolphin
    from .elephant import elephant
    from .owl import owl

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    app.register_blueprint(turtle,url_prefix='/t')
    app.register_blueprint(elephant,url_prefix='/e')
    app.register_blueprint(owl,url_prefix='/o')
    app.register_blueprint(dolphin,url_prefix='/d')


    return app

