from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from models import Users

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
        existing_user = Users.query.filter((Users.username == username) | (Users.email == email)).first()
        if existing_user is not None:
            return jsonify(message="Selle kasutajanime või e-posti aadressiga kasutaja on juba olemas"), 401

        user = Users(
            username=username,
            email=email,
            description="This is a placeholder description",
            image_url="",
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

        user = Users.authenticate(username, password) 

        if user:
            access_token = create_access_token(identity=user.id)
            user_data = {'user_id': user.id, 'username': user.username, 'email': user.email, 'image_url': user.image_url}
            
            response = jsonify(user=user_data)
            set_access_cookies(response, access_token)
            
            return response, 201
        
        else:
            return jsonify(message="Vale kasutajanimi või salasõna"), 401
        
    except Exception as e:
        return jsonify(message="An error occurred while processing your request."), 500

@auth.route('/logout', methods=['POST'])
def logout():
    try:
        response = jsonify()
        unset_jwt_cookies(response)
        return response, 200
    except Exception as e:
        return jsonify(message="An error occurred while processing your request."), 500

@auth.route('/check_token', methods=['POST'])
@jwt_required(locations=["cookies"])
def check_token():
    try:
        current_user_id = get_jwt_identity()
        
        user = Users.query.get(current_user_id)
        username = user.username if user else None
        image_url = user.image_url
        
        return jsonify(message="Token is valid", user_id=current_user_id, username=username, image_url=image_url), 200
    except Exception as e:
        return jsonify(message="Token validation failed"), 401