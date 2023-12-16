from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import ShoppingCarts, Payments, Sales, Loans, db
from datetime import datetime, timedelta

payment = Blueprint('payment', __name__)

@payment.route('/make_payment', methods=['POST'])
@jwt_required(locations=["cookies"])
def make_payment():
    user_id = get_jwt_identity()

    # Retrieve shopping cart for the user
    shopping_cart = ShoppingCarts.query.filter_by(user_id=user_id).first()

    if not shopping_cart:
        return jsonify({'message': 'Shopping cart not found for the user'}), 404

    # Calculate the total price of items in the shopping cart
    total_price = sum(cart_item.post.price * cart_item.quantity for cart_item in shopping_cart.cart_items)

    # Retrieve payment details from the request
    payment_data = request.get_json()
    first_name = payment_data.get('first_name')
    last_name = payment_data.get('last_name')
    address = payment_data.get('address')
    city = payment_data.get('city')
    postal_code = payment_data.get('postal_code')
    
    if len(first_name) > 50 or len(last_name) > 50 or len(address) > 255 or len(city) > 100 or len(postal_code) > 20:
        return jsonify({'message': 'Invalid input length. Please ensure that all fields comply with the length limits.'})

    # Calculate payment date as the date next month
    payment_date = datetime.utcnow() + timedelta(days=30)
    payment_date_str = payment_date.strftime('%d.%m.%Y')

    # Create a payment entry in the database
    payment = Payments(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        address=address,
        city=city,
        postal_code=postal_code,
        amount=total_price,
        payment_date_epoch=str(payment_date.timestamp()),
        payment_date_str=payment_date_str
    )

    # Add payment to the database
    db.session.add(payment)
    db.session.commit()

    # Delete items from the shopping cart and add entries to other tables
    for cart_item in shopping_cart.cart_items:
        # Add entry to Loans table
        loan = Loans(
            lender_user_id=user_id,
            borrower_user_id=cart_item.post.user_id,
            post_id=cart_item.post_id,
            quantity=cart_item.quantity,
            payment_id=payment.payment_id
        )
        db.session.add(loan)

        # Add entry to Sales table
        sale = Sales(
            seller_user_id=cart_item.post.user_id,
            buyer_user_id=user_id,
            post_id=cart_item.post_id,
            quantity=cart_item.quantity,
            payment_id=payment.payment_id
        )
        db.session.add(sale)

    

        # Delete cart item
        db.session.delete(cart_item)

    # Commit changes to the database
    db.session.commit()

    return jsonify({'success': 'Payment successful'})

