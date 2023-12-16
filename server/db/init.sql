CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    email VARCHAR(150) NOT NULL,
    password VARCHAR(350) NOT NULL,
    description TEXT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    create_date_epoch BIGINT NOT NULL,
    create_date_str VARCHAR(50) NOT NULL,
    role ENUM('user', 'admin', 'super admin') NOT NULL DEFAULT 'user',
    is_banned BOOLEAN NOT NULL DEFAULT FALSE,
    ban_expiry_epoch BIGINT
);

CREATE TABLE IF NOT EXISTS posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    price INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    short_description VARCHAR(255) NOT NULL,
    long_description TEXT NOT NULL,
    youtube_url VARCHAR(255),
    category VARCHAR(100) NOT NULL,
    sub_category VARCHAR(100) NOT NULL,
    key_value_pairs JSON,
    post_date BIGINT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT,
    image_url VARCHAR(255) NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
);

CREATE TABLE IF NOT EXISTS shopping_carts (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS cart_items (
    cart_item_id INT AUTO_INCREMENT PRIMARY KEY,
    cart_id INT,
    post_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES shopping_carts(cart_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
);

CREATE TABLE IF NOT EXISTS complaints (
    complaint_id INT AUTO_INCREMENT PRIMARY KEY,
    post_or_user_id INT NOT NULL,
    is_post_complaint BOOLEAN NOT NULL,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    accuser_id INT,
    accused_id INT,
    reporters_complaints TEXT NOT NULL,
    severity ENUM('low', 'medium', 'high'),
    FOREIGN KEY (accuser_id) REFERENCES users(id),
    FOREIGN KEY (accused_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date_epoch BIGINT NOT NULL,
    payment_date_str VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    lender_user_id INT NOT NULL,
    borrower_user_id INT NOT NULL,
    post_id INT,
    quantity INT NOT NULL,
    payment_id INT NOT NULL,
    FOREIGN KEY (lender_user_id) REFERENCES users(id),
    FOREIGN KEY (borrower_user_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id),
    FOREIGN KEY (payment_id) REFERENCES payments(payment_id)
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    seller_user_id INT NOT NULL,
    buyer_user_id INT NOT NULL,
    post_id INT,
    quantity INT NOT NULL,
    payment_id INT NOT NULL,
    is_sent BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (seller_user_id) REFERENCES users(id),
    FOREIGN KEY (buyer_user_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id),
    FOREIGN KEY (payment_id) REFERENCES payments(payment_id)
);

