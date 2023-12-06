from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Users, Posts, Complaints, db

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
                "is_banned": user.is_banned
            })

        return jsonify(users_data), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


@admin.route('/get_all_complaints', methods=['GET'])
@jwt_required(locations=["cookies"])
def get_complaints():
    """
    Get all complaints.

    Returns:
    - json: A JSON response containing the list of complaints.
    """
    try:
        complaints = Complaints.query.all()

        # Convert SQLAlchemy model instances to dictionaries
        complaints_list = []
        for complaint in complaints:
            # Fetch usernames from Users table
            accuser = Users.query.get(complaint.accuser_id)
            accused = Users.query.get(complaint.accused_id)

             # Check if it's a post complaint and if the post exists
            is_post_complaint = complaint.is_post_complaint
            post_exists = False
            if is_post_complaint:
                post_exists = Posts.query.filter_by(post_id=complaint.post_or_user_id).first() is not None
            
            
            # Create dictionary representation of the complaint
            complaint_dict = {
                "id": complaint.complaint_id,
                "post_or_user_id": complaint.post_or_user_id,
                "is_post_complaint": complaint.is_post_complaint,
                "post_exists": post_exists,
                "title": complaint.title,
                "category": complaint.category,
                "accuser_id": complaint.accuser_id,
                "accuser_username": accuser.username,
                "accuser_email": accuser.email,
                "accused_id": complaint.accused_id,
                "accused_username": accused.username,
                "accused_email": accused.email,
                "reporters_complaints": complaint.reporters_complaints,
                "severity": complaint.severity,
                "is_banned": accused.is_banned,
            }
            complaints_list.append(complaint_dict)

        return jsonify(complaints_list), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


@admin.route('/change_to_admin', methods=["POST"])
@jwt_required(locations=["cookies"])
def change_to_admin():
    """
    Change a user to a admin.
    """
    try:
        current_user_id = get_jwt_identity()
        current_user = Users.query.filter_by(id=current_user_id).first()
        
        if not current_user or current_user.role != "super admin":
            return jsonify({"message": "You do not have the permission to change the role of a user"}), 403
        
        data = request.get_json()
        target_user_id = data.get("target_user_id")
        
        target_user = Users.query.get(target_user_id)
        target_user.role = "admin"
        
        db.session.commit()
        
        return jsonify({"message": "User role changed successfully"}), 200
        
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


@admin.route('/demote_to_user', methods=["POST"])
@jwt_required(locations=["cookies"])
def demote_to_user():
    """
    Demote an admin to a user.
    """
    try:
        current_user_id = get_jwt_identity()
        current_user = Users.query.filter_by(id=current_user_id).first()

        # Check if the current user is a super admin
        if not current_user or current_user.role != "super admin":
            return jsonify({"error": "You do not have the permission to demote a user"}), 403

        # Get target user ID from the request JSON payload
        data = request.get_json()
        target_user_id = data.get("target_user_id")

        # Validate input (ensure target_user_id is provided and exists)
        if not target_user_id:
            return jsonify({"error": "Target user ID is required"}), 400

        target_user = Users.query.get(target_user_id)

        # Check if the target user exists
        if not target_user:
            return jsonify({"error": "Target user not found"}), 404

        # Check if the target user is currently an admin
        if target_user.role != "admin":
            return jsonify({"error": "Target user is not currently an admin"}), 400

        # Demote the target user to a regular user
        target_user.role = "user"

        # Commit the changes to the database
        db.session.commit()

        return jsonify({"message": "User demoted successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@admin.route('/ban_user', methods=["POST"])
@jwt_required(locations=["cookies"])
def ban_user():
    """
    Ban a user.
    """
    try:
        current_user_id = get_jwt_identity()
        current_user = Users.query.filter_by(id=current_user_id).first()

        # Check if the current user is a super admin
        if not current_user or current_user.role != "super admin":
            return jsonify({"message": "You do not have the permission to ban a user"}), 403

        # Get target user ID from the request JSON payload
        data = request.get_json()
        target_user_id = data.get("target_user_id")
        time_expiry = data.get("time_expiry")

        # Validate input (ensure target_user_id is provided and exists)
        if not target_user_id:
            return jsonify({"error": "Target user ID is required"}), 400
        
        if current_user_id == target_user_id:
            return jsonify({"message": "You can't ban yourself"})

        target_user = Users.query.get(target_user_id)

        # Check if the target user exists
        if not target_user:
            return jsonify({"error": "Target user not found"}), 404

        # Ban the user
        target_user.is_banned = True
        
        # Set the time expiry if provided
        if time_expiry is not None:
            target_user.ban_expiry_epoch = time_expiry

        # Commit the changes to the database
        db.session.commit()

        return jsonify({"message": "User banned successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@admin.route('/unban_user', methods=["POST"])
@jwt_required(locations=["cookies"])
def unban_user():
    """
    Unban a user.
    """
    try:
        current_user_id = get_jwt_identity()
        current_user = Users.query.filter_by(id=current_user_id).first()

        # Check if the current user is a super admin
        if not current_user or current_user.role != "super admin":
            return jsonify({"message": "You do not have the permission to unban a user"}), 403

        # Get target user ID from the request JSON payload
        data = request.get_json()
        target_user_id = data.get("target_user_id")

        # Validate input (ensure target_user_id is provided and exists)
        if not target_user_id:
            return jsonify({"error": "Target user ID is required"}), 400

        # Check if the user is trying to unban themselves
        if current_user_id == target_user_id:
            return jsonify({"message": "You can't unban yourself"})

        target_user = Users.query.get(target_user_id)

        # Check if the target user exists
        if not target_user:
            return jsonify({"error": "Target user not found"}), 404

        # Unban the user
        target_user.is_banned = False
        target_user.time_expiry_epoch = None  # Reset time_expiry

        # Commit the changes to the database
        db.session.commit()

        return jsonify({"message": "User unbanned successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@admin.route('/delete_complaint', methods=['POST'])
@jwt_required(locations=["cookies"])
def delete_complaint():
    """
    Delete a complaint.

    Returns:
    - json: A JSON response indicating the success or failure of the operation.
    """
    try:
        current_user_id = get_jwt_identity()
        current_user = Users.query.filter_by(id=current_user_id).first()

        # Check if the current user is an admin or super admin
        if not current_user or current_user.role not in ['admin', 'super admin']:
            return jsonify({"message": "You do not have permission to access this resource"}), 403

        # Get complaint ID from the request JSON payload
        data = request.get_json()
        complaint_id = data.get('complaint_id')

        if not complaint_id or not str(complaint_id).isnumeric():
            return jsonify({"message": "Invalid complaint ID"}), 400

        # Check if the complaint exists
        complaint = Complaints.query.get(int(complaint_id))
        if not complaint:
            return jsonify({"message": "Complaint not found"}), 404

        # Delete the complaint
        db.session.delete(complaint)
        db.session.commit()

        return jsonify({"message": "Complaint deleted successfully"}), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
