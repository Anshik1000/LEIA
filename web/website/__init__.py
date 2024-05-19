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

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')


    return app

