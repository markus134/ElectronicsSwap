from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta
import secrets
from flask_cors import CORS 

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__, static_url_path='/static')

    # Enable CORS 
    CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

    app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql-db/website'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False # Change this in production
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000 # Don't allow files bigger than 16 megabytes to be uploaded

    
    # Initialize the extensions within the application context
    db.init_app(app)
    jwt.init_app(app)

    # Import and register blueprints
    from auth import auth  # This is here to avoid a circular import
    from profile import profile
    from posts import posts
    
    app.register_blueprint(auth, url_prefix="/api/auth")
    app.register_blueprint(profile, url_prefix="/api/profile")
    app.register_blueprint(posts, url_prefix="/api/posts")

    return app
