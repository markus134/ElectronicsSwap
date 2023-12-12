from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta
import secrets
import time
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_cors import CORS 

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__, static_url_path='/static')

    # Enable CORS 
    CORS(app, supports_credentials=True, origins=["http://localhost"])

    app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql-db/website'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000 # Don't allow files bigger than 16 megabytes to be uploaded

    
    # Initialize the extensions within the application context
    db.init_app(app)
    jwt.init_app(app)
    
    
    from models import Users
    
    # Wait for MySQL, there's probably a better way to do this
    time.sleep(15)
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()

        # Check if there is a super admin, and create one if not
        super_admin = Users.query.filter_by(role='super admin').first()
        if super_admin is None:
            # Create a default super admin
            default_super_admin = Users(
                username="admin",
                email="admin@gmail.com",
                description="This is a placeholder description",
                image_url="",
                role="super admin",
                password=generate_password_hash("averysecurepassword"),
                create_date_epoch=str(datetime.utcnow().timestamp()),
                create_date_str = datetime.utcnow().strftime("%B %d, %Y %H:%M:%S %Z") + " UTC",
            )
            default_super_admin.add()
        

    # Import and register blueprints
    from auth import auth  # This is here to avoid a circular import
    from profile import profile
    from posts import posts
    from admin import admin
    
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(profile, url_prefix="/profile")
    app.register_blueprint(posts, url_prefix="/posts")
    app.register_blueprint(admin, url_prefix="/admin")

    return app
