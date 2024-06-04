CREATE DATABASE CustomerDatabase;

USE CustomerDatabase;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    left_eye_degree DECIMAL(5, 2) NOT NULL,
    right_eye_degree DECIMAL(5, 2) NOT NULL
);
