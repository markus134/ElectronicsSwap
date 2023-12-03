from __init__ import db
from werkzeug.security import check_password_hash


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    image_url = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.Enum('user', 'admin', 'super admin'), default='user', nullable=False)
    create_date_epoch = db.Column(db.Float)
    create_date_str = db.Column(db.String)

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
    post_date = db.Column(db.Float)
    
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

class ShoppingCarts(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    user = db.relationship('Users', backref=db.backref('shopping_cart', uselist=False, lazy=True))

    def add(self):
        db.session.add(self)
        db.session.commit()


class CartItems(db.Model):
    cart_item_id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('shopping_carts.cart_id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    cart = db.relationship('ShoppingCarts', backref=db.backref('cart_items', lazy=True))
    post = db.relationship('Posts', backref=db.backref('cart_items', lazy=True))

    def add(self):
        db.session.add(self)
        db.session.commit()


class Complaints(db.Model):
    complaint_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    accuser_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    accused_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reporters_complaints = db.Column(db.Text, nullable=False)
    severity = db.Column(db.Enum('low', 'medium', 'high'), nullable=False)
    
    accuser = db.relationship('Users', foreign_keys=[accuser_id], backref=db.backref('accuser_complaints', lazy=True))
    accused = db.relationship('Users', foreign_keys=[accused_id], backref=db.backref('accused_complaints', lazy=True))

    def add(self):
        db.session.add(self)
        db.session.commit()
