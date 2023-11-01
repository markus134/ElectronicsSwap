from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta
import secrets
<<<<<<< HEAD
from flask_cors import CORS 
=======
>>>>>>> 25cf25fdbfe3568b0059505b757fc98fba6c6477

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

<<<<<<< HEAD
    # Enable CORS with specific options
    CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

    app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql-db/users'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
=======
    app.config['JWT_SECRET_KEY'] = secrets.token_hex(32) # Secret key should be random
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql-db/users'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1) # JWT cookie should expire in an hour
>>>>>>> 25cf25fdbfe3568b0059505b757fc98fba6c6477
    
    # Initialize the extensions within the application context
    db.init_app(app)
    jwt.init_app(app)

    # Import and register blueprints
<<<<<<< HEAD
    from auth import auth  # This is here to avoid a circular import
=======
    from auth import auth # This is here to avoid a circular import
    
>>>>>>> 25cf25fdbfe3568b0059505b757fc98fba6c6477
    app.register_blueprint(auth, url_prefix="/api/auth")

    return app
