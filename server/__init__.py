from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import jwt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration settings should be placed in a separate configuration file or environment variables
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql-db/users'
    
    # Initialize the extensions within the application context
    db.init_app(app)
    jwt.init_app(app)

    # Import and register blueprints
    from auth import auth
    app.register_blueprint(auth, url_prefix="/api/auth")

    return app
