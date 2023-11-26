CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    email VARCHAR(150) NOT NULL,
    password VARCHAR(350) NOT NULL,
    description TEXT NOT NULL,
    image_url VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    price INT NOT NULL,
    title VARCHAR (255) NOT NULL,
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
