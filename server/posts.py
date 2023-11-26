from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Users, Images, Posts, db
import os
from datetime import datetime
from werkzeug.utils import secure_filename

posts = Blueprint('posts', __name__)

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
API_URL = 'http://localhost:5000/'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@posts.route('/create_post', methods=['POST'])
@jwt_required(locations=["cookies"])
def create_post():
    try:
        user_id = get_jwt_identity()

        data = request.form
        title = data.get('productTitle')
        price = data.get('price')
        short_description = data.get('short_description')
        long_description = data.get('long_description')
        youtube_url = data.get('youtube_url')
        category = data.get('category')
        sub_category = data.get('sub_category')
        key_value_pairs = data.get('key_value_pairs')

        # Check if the required fields are present
        if not price:
            return jsonify({"message": "You need to set a price."}), 400
        
        if not price.isnumeric():
            return jsonify({"message": "The price needs to be an integer."}), 400
        
        if not title:
            return jsonify({"message": "You need to set a title."}), 400
            
        if not category or not sub_category:
            return jsonify({"message": "A category or subcategory is missing"}), 400
        
        if not short_description or not long_description:
            return jsonify({"message": "Short and long descriptions are required"}), 400

        user = Users.query.filter_by(id=user_id).first()

        if not user:
            return jsonify({"message": "User not found"}), 404

        post = Posts(
            user_id=user_id,
            title=title,
            price=price,
            short_description=short_description,
            long_description=long_description,
            youtube_url=youtube_url,
            category=category,
            sub_category=sub_category,
            key_value_pairs=key_value_pairs,
            post_date=str(datetime.utcnow().timestamp())
        )

        db.session.add(post)
        db.session.commit()

        # Handle image uploads
        for file in request.files.values():
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))

                image = Images(
                    post_id=post.post_id,
                    image_url=os.path.join(API_URL, UPLOAD_FOLDER, filename)
                )

                db.session.add(image)
                db.session.commit()

        return jsonify({"message": "Post and images created successfully"}), 201

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@posts.route('/get_posts', methods=['GET'])
def get_posts():
    posts = Posts.query.all()
    result = []

    for post in posts:
        first_image = Images.query.filter_by(post_id=post.post_id).first()
        image_url = first_image.image_url if first_image else None
        
        result.append({
            "post_id": post.post_id,
            "title": post.title,
            "price": post.price,
            "date": post.post_date,
            "short_description": post.short_description,
            "category": post.category,
            "subcategory": post.sub_category,
            "image_url": image_url,
            "user_id": post.user_id,
        })

    return jsonify(result), 200

@posts.route('/get_post', methods=['POST'])
def get_post():
    try:
        # Get post id
        data = request.get_json()
        post_id = data.get('postId')

        if not post_id or not post_id.isnumeric():
            return jsonify({"message": "Invalid post ID"}), 400

        # Fetch the post
        post = Posts.query.get(int(post_id))

        if not post:
            return jsonify({"message": "Post not found"}), 404

        # Get all images related to the post
        images = Images.query.filter_by(post_id=post.post_id).all()
        image_urls = [image.image_url for image in images]

        # Get the post author's information
        user = Users.query.filter_by(id=post.user_id).first()

        if user:
            author_data = {
                "user_id": user.id,
                "username": user.username,
                "profile_picture_url": user.image_url,
            }
        else:
            return jsonify({"message": "Post author not found"})

        # Construct the post data
        post_data = {
            "post_id": post.post_id,
            "title": post.title,
            "price": post.price,
            "date": post.post_date,
            "short_description": post.short_description,
            "long_description": post.long_description,
            "youtube_url": post.youtube_url,
            "category": post.category,
            "subcategory": post.sub_category,
            "key_value_pairs": post.key_value_pairs,
            "image_urls": image_urls,
            "author": author_data,
        }

        return jsonify(post_data), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

