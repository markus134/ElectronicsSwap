from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, unset_jwt_cookies, jwt_required
from werkzeug.security import generate_password_hash
from models import User 

auth = Blueprint('auth', __name__)

@auth.route('/registration', methods=['POST'])
def registration():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )

        user.add()

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response = jsonify()
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return response, 201
    else:
        return jsonify(message="User already exists."), 400

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.authenticate(username, password) 

    if user:
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response = jsonify()
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response, 201
    else:
        return jsonify(message="Unauthorized"), 401

@auth.route('/logout', methods=['POST'])
@jwt_required
def logout():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200
