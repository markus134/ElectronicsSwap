from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import jwt


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'wajfowajfowaofjwaofjwaojfoajwf'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/users'
    db.init_app(app)
    jwt.init_app(app)
    
    from auth import auth
    
    app.register_blueprint(auth, url_prefix="/api/auth")
    
    return app
