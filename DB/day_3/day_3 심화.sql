USE oz_assignment;

CREATE TABLE orders(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    product_name VARCHAR(255),
    quantity INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    );