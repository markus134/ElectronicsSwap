from __init__ import db
from werkzeug.security import check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String, unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user
        return None