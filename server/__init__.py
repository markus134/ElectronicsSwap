from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta
import secrets

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = secrets.token_hex(32) # Secret key should be random
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql-db/users'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1) # JWT cookie should expire in an hour
    
    # Initialize the extensions within the application context
    db.init_app(app)
    jwt.init_app(app)

    # Import and register blueprints
    from auth import auth # This is here to avoid a circular import
    
    app.register_blueprint(auth, url_prefix="/api/auth")

    return app
