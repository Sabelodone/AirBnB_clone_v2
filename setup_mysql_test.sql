-- Create Database if it doesn't exist
-- Create User 'hbnb_test' if it doesn't exist, setting the password to 'hbnb_test_pwd'
-- Grant all privileges on 'hbnb_test_db' to 'hbnb_test' user
-- Grant SELECT privilege on 'performance_schema' to 'hbnb_test' user

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
