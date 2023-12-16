from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Users, Loans, Payments, Sales, Posts, Images, db
import os
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, API_URL

profile = Blueprint('profile', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@profile.route('/get_user', methods=["POST"])
@jwt_required(optional=True, locations=["cookies"])
def get_user():
    data = request.get_json()
    
    user_id = get_jwt_identity()
    target_user_id = data.get('id')
    
    if not target_user_id:
        return jsonify("You haven't set an id.")

    user = Users.query.get(target_user_id)

    if not user:
        return jsonify("There is no user with that id.")
    
    if int(user_id) == int(target_user_id):
        return jsonify(id=user.id, username=user.username, email=user.email, description=user.description, image_url=user.image_url)
    
    return jsonify(id=user.id, username=user.username, description=user.description, image_url=user.image_url)


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

    user = Users.query.get(current_user_id)

    if not user:
        return jsonify("User not found.")

    if new_username:
        user.username = new_username
    if new_description:
        user.description = new_description
    if new_email:
        user.email = new_email
    if 'file' in request.files and allowed_file(file.filename):
        user.image_url = API_URL + "/static/" + file_path  # Store the file path in the database

    # Commit changes to the database
    user.change_user_info()

    return jsonify(message="User information updated successfully.", image_url=user.image_url)


@profile.route('/get_loans', methods=["POST"])
@jwt_required(locations=["cookies"])
def get_loans():
    current_user_id = get_jwt_identity()
    
    loans = Loans.query.filter(Loans.lender_user_id == current_user_id).all()
    loans_list = []
    for loan in loans:
        post_info = Posts.query.get(loan.post_id)
        lender_info = Users.query.get(loan.borrower_user_id)
        loan_date_str = Payments.query.get(loan.payment_id).payment_date_str
        first_image = Images.query.filter_by(post_id=loan.post_id).first()
        image_url = first_image.image_url if first_image else None
        
        loans_list.append({
            'loan_id': loan.loan_id,
            'lender_user_id': loan.lender_user_id,
            'borrower_user_id': loan.borrower_user_id,
            'post_id': loan.post_id,
            'quantity': loan.quantity,
            'loan_date_str': loan_date_str,
            'post_info': {
                'title': post_info.title,
                'price': post_info.price,
                'image_url': image_url
            },
            'lender_username': lender_info.username,
        })
    return jsonify(loans_list)

@profile.route('/get_sales', methods=["POST"])
@jwt_required(locations=["cookies"])
def get_sales():
    data = request.get_json()
    
    sent_sales = data.get("sent_sales")
    current_user_id = get_jwt_identity()
    
    sales = Sales.query.filter(Sales.seller_user_id == current_user_id).all()
    if sent_sales:
        sales = [sale for sale in sales if sale.is_sent]
    else:
        sales = [sale for sale in sales if not sale.is_sent]
    
    sales_list = []
    for sale in sales:
        post_info = Posts.query.get(sale.post_id)
        buyer_info = Users.query.get(sale.buyer_user_id)
        payment = Payments.query.get(sale.payment_id)
        first_image = Images.query.filter_by(post_id=sale.post_id).first()
        image_url = first_image.image_url if first_image else None
        
        sales_list.append({
            'sale_id': sale.sale_id,
            'seller_user_id': sale.seller_user_id,
            'buyer_user_id': sale.buyer_user_id,
            'post_id': sale.post_id,
            'quantity': sale.quantity,
            'loan_date_str': payment.payment_date_str,
            'address': payment.address,
            'first_name': payment.first_name,
            'last_name': payment.last_name,
            'city': payment.city,
            'postal_code': payment.postal_code,
            'post_info': {
                'title': post_info.title,
                'price': post_info.price,
                'image_url': image_url
            },
            'borrower_username': buyer_info.username,
        })
    return jsonify(sales_list)


@profile.route('/mark_sale_as_sent', methods=["POST"])
@jwt_required(locations=["cookies"])
def mark_sale_as_sent():
    data = request.get_json()
    
    sale_id = data.get("sale_id")
    current_user_id = get_jwt_identity()
    

    sale = Sales.query.filter_by(sale_id=sale_id, seller_user_id=current_user_id).first()

    if not sale:
        return jsonify("Sale not found or unauthorized access.")

    sale.is_sent = True

    # Commit changes to the database
    db.session.commit()

    return jsonify(message="Sale marked as unsent successfully.", is_sent=sale.is_sent)
