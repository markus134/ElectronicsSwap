from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Users

admin = Blueprint('admin', __name__)

@admin.route('/get_all_users', methods=['GET'])
@jwt_required(locations=["cookies"])
def get_all_users():
    try:
        # Check if the user making the request is an admin or super admin
        current_user_id = get_jwt_identity()
        current_user = Users.query.filter_by(id=current_user_id).first()

        if not current_user or current_user.role not in ['admin', 'super admin']:
            return jsonify({"message": "You do not have permission to access this resource"}), 403

        # Retrieve all users from the database
        all_users = Users.query.all()

        # Create a list to store user data
        users_data = []

        # Iterate through all users and extract relevant information
        for user in all_users:
            users_data.append({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "description": user.description,
                "image_url": user.image_url,
                "role": user.role,
                "createdAt": user.create_date_str,
            })

        return jsonify(users_data), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500