from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies, jwt_required
from werkzeug.security import generate_password_hash
from models import User 

auth = Blueprint('auth', __name__)

@auth.route('/registration', methods=['POST'])
def registration():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check for missing fields in the request data
        if not username or not email or not password:
            return jsonify(message="Puudub kasutajanimi, e-mail või parool"), 401

        # Check if the user with the given username or email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user is not None:
            return jsonify(message="Selle kasutajanime või e-posti aadressiga kasutaja on juba olemas"), 401

        user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        user.add()
        
        access_token = create_access_token(identity=user.id)
        response = jsonify()
        set_access_cookies(response, access_token)
        
        return response, 201
    
    except Exception as e:
        return jsonify(message="An error occurred while processing your request." + str(e)), 500

@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify(message="Puudub kasutajanimi või parool"), 401

        user = User.authenticate(username, password) 

        if user:
            access_token = create_access_token(identity=user.id)
            response = jsonify()
            set_access_cookies(response, access_token)
            
            return response, 201
        
        else:
            return jsonify(message="Vale kasutajanimi või salasõna"), 401
        
    except Exception as e:
        return jsonify(message="An error occurred while processing your request."), 500

@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    try:
        response = jsonify()
        unset_jwt_cookies(response)
        return response, 200
    except Exception as e:
        return jsonify(message="An error occurred while processing your request."), 500
