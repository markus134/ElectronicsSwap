from flask import Blueprint, request, jsonify, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User
import os
from werkzeug.utils import secure_filename

profile = Blueprint('profile', __name__)

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
API_URL = 'http://localhost:5000/'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@profile.route('/get_user', methods=["POST"])
def get_user():
    data = request.get_json()
    user_id = data.get('id')
    
    if not user_id:
        return jsonify("You haven't set an id.")

    user = User.query.get(user_id)

    if not user:
        return jsonify("There is no user with that id.")
    
    return jsonify(id=user.id, username=user.username, description=user.description, email=user.email, image_url=user.image_url)


@profile.route('/change_user_info', methods=["POST"])
@jwt_required(locations=["cookies"])
def change_user_info():
    
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        
    current_user_id = get_jwt_identity()

    data = request.form  # Access form data, including files

    new_username = data.get('username')
    new_description = data.get('description')
    new_email = data.get('email')

    # Check if the post request has the file part
    if 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

    user = User.query.get(current_user_id)

    if not user:
        return jsonify("User not found.")

    if new_username:
        user.username = new_username
    if new_description:
        user.description = new_description
    if new_email:
        user.email = new_email
    if 'file' in request.files and allowed_file(file.filename):
        user.image_url = API_URL + file_path  # Store the file path in the database

    # Commit changes to the database
    user.change_user_info()

    return jsonify(message="User information updated successfully.", image_url=user.image_url)
