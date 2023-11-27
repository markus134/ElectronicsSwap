from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Users, Images, Posts, ShoppingCarts, CartItems, db
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, API_URL

posts = Blueprint('posts', __name__)

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
        
         # Verify YouTube URL and update if needed
        if youtube_url:
            if not youtube_url.startswith('https://www.youtube.com/'):
                return jsonify({"message": "Invalid YouTube URL format"}), 400

            # Replace 'watch?v=' with 'embed'
            youtube_url = youtube_url.replace('watch?v=', 'embed/')

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

@posts.route('/get_user_posts', methods=['GET'])
@jwt_required(locations=["cookies"])
def get_user_posts():
    try:
        user_id = get_jwt_identity()

        # Retrieve posts created by the authenticated user
        user_posts = Posts.query.filter_by(user_id=user_id).all()
        result = []

        for post in user_posts:
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

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

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

@posts.route('/delete_user_post', methods=['POST'])
@jwt_required(locations=["cookies"])
def delete_user_post():
    try:
        user_id = get_jwt_identity()

        data = request.get_json()
        post_id = data.get('post_id')

        if not post_id or not str(post_id).isnumeric():
            return jsonify({"message": "Invalid post ID"}), 400

        post = Posts.query.get(int(post_id))

        if not post:
            return jsonify({"message": "Post not found"}), 404

        # Ensure that the user requesting the deletion is the owner of the post
        if post.user_id != user_id:
            return jsonify({"message": "You do not have permission to delete this post"}), 403

        # Delete related images
        images = Images.query.filter_by(post_id=post.post_id).all()
        for image in images:
            db.session.delete(image)

        # Delete the post
        db.session.delete(post)
        db.session.commit()

        return jsonify({"message": "Post and associated images deleted successfully"}), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@posts.route('/add_to_cart', methods=['POST'])
@jwt_required(locations=["cookies"])
def add_to_cart():
    try:
        user_id = get_jwt_identity()

        data = request.get_json()
        post_id = data.get('post_id')
        quantity = data.get('quantity', 1)
        
        if not quantity > 0:
            return jsonify({"message": "Quantity must be positive"})

        if not post_id or not str(post_id).isnumeric():
            return jsonify({"message": "Invalid post ID"}), 400

        post = Posts.query.get(int(post_id))

        if not post:
            return jsonify({"message": "Post not found"}), 404

        user_cart = ShoppingCarts.query.filter_by(user_id=user_id).first()

        if not user_cart:
            user_cart = ShoppingCarts(user_id=user_id)
            db.session.add(user_cart)
            db.session.commit()

        cart_item = CartItems.query.filter_by(cart_id=user_cart.cart_id, post_id=post.post_id).first()

        if cart_item:
            cart_item.quantity += int(quantity)
        else:
            cart_item = CartItems(cart_id=user_cart.cart_id, post_id=post.post_id, quantity=int(quantity))
            db.session.add(cart_item)

        db.session.commit()

        return jsonify({"message": "Product added to the cart successfully"}), 201

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@posts.route('/get_cart', methods=['POST'])
@jwt_required(locations=["cookies"])
def get_cart():
    try:
        user_id = get_jwt_identity()

        user_cart = ShoppingCarts.query.filter_by(user_id=user_id).first()

        if not user_cart:
            return jsonify({"message": "Shopping cart is empty"}), 200

        cart_items = CartItems.query.filter_by(cart_id=user_cart.cart_id).all()
        result = []

        for cart_item in cart_items:
            post = Posts.query.get(cart_item.post_id)

            if post:
                # Fetch the first image for the post
                first_image = Images.query.filter_by(post_id=post.post_id).first()
                image_url = first_image.image_url if first_image else None

                # Fetch the author's username
                author = Users.query.get(post.user_id)
                author_username = author.username if author else None

                result.append({
                    "post_id": post.post_id,
                    "title": post.title,
                    "price": post.price,
                    "quantity": cart_item.quantity,
                    "image_url": image_url,
                    "seller": author_username,
                })

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@posts.route('/update_quantity', methods=['POST'])
@jwt_required(locations=["cookies"])
def update_quantity():
    try:
        user_id = get_jwt_identity()

        data = request.get_json()
        post_id = data.get('post_id')

        if not post_id or not str(post_id).isnumeric():
            return jsonify({"message": "Invalid post ID"}), 400

        quantity = data.get('quantity', 0)

        if not isinstance(quantity, int) or quantity == 0:
            return jsonify({"message": "Invalid quantity"}), 400

        user_cart = ShoppingCarts.query.filter_by(user_id=user_id).first()

        if not user_cart:
            return jsonify({"message": "Shopping cart is empty"}), 400

        cart_item = CartItems.query.filter_by(cart_id=user_cart.cart_id, post_id=post_id).first()

        if cart_item:
            new_quantity = cart_item.quantity + quantity

            if new_quantity > 0:
                cart_item.quantity = new_quantity
                db.session.commit()
                return jsonify({"message": f"Quantity updated successfully to {new_quantity}"}), 200
            else:
                return jsonify({"message": "Invalid quantity to update"}), 400
        else:
            return jsonify({"message": "Item not found in the shopping cart"}), 404

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@posts.route('/delete_product', methods=['POST'])
@jwt_required(locations=["cookies"])
def delete_product():
    try:
        user_id = get_jwt_identity()

        data = request.get_json()
        post_id = data.get('post_id')

        if not post_id or not str(post_id).isnumeric():
            return jsonify({"message": "Invalid post ID"}), 400

        post = Posts.query.get(int(post_id))

        if not post:
            return jsonify({"message": "Post not found"}), 404

        user_cart = ShoppingCarts.query.filter_by(user_id=user_id).first()

        if not user_cart:
            return jsonify({"message": "Shopping cart is empty"}), 400

        cart_item = CartItems.query.filter_by(cart_id=user_cart.cart_id, post_id=post.post_id).first()

        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            return jsonify({"message": "Product deleted from cart successfully"}), 200
        else:
            return jsonify({"message": "Product not found in the cart"}), 404

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@posts.route('/delete_all_products', methods=['POST'])
@jwt_required(locations=["cookies"])
def delete_all_products():
    try:
        user_id = get_jwt_identity()

        user_cart = ShoppingCarts.query.filter_by(user_id=user_id).first()

        if not user_cart:
            return jsonify({"message": "Shopping cart is empty"}), 200

        cart_items = CartItems.query.filter_by(cart_id=user_cart.cart_id).all()

        if cart_items:
            for cart_item in cart_items:
                db.session.delete(cart_item)

            db.session.commit()
            return jsonify({"message": "All items deleted from cart successfully"}), 200
        else:
            return jsonify({"message": "Shopping cart is already empty"}), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

