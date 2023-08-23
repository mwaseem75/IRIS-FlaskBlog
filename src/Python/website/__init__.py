from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_login import LoginManager
from .myconfig import * 

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "iris-FlaskBlogKey"
    #Getting DB parameters from myconfig.py file
    app.config['SQLALCHEMY_DATABASE_URI'] = 'iris://'+DB_USER+':'+DB_PASS+'@'+DB_URL+':'+DB_PORT+'/'+DB_NAMESPACE
    app.app_context().push()   
       
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    db.init_app(app)
    with app.app_context():
        db.create_all()

    #Assign Login View 
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
