from __init__ import db
from werkzeug.security import check_password_hash
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    image_url = db.Column(db.String)
    password = db.Column(db.String)
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def change_user_info(self):
        db.session.commit()
        
    @staticmethod
    def authenticate(username, password):
        user = Users.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user
        return None

class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    short_description = db.Column(db.String, nullable=False)
    long_description = db.Column(db.Text, nullable=False)
    youtube_url = db.Column(db.String)
    category = db.Column(db.String, nullable=False)
    sub_category = db.Column(db.String, nullable=False)
    key_value_pairs = db.Column(db.JSON)
    post_date = db.Column(db.Float, server_default=str(datetime.utcnow().timestamp()))
    
    user = db.relationship('Users', backref=db.backref('posts', lazy=True))

    def add(self):
        db.session.add(self)
        db.session.commit()

class Images(db.Model):
    image_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    image_url = db.Column(db.String, nullable=False)

    post = db.relationship('Posts', backref=db.backref('images', lazy=True))

    def add(self):
        db.session.add(self)
        db.session.commit()