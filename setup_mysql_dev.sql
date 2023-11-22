# Script to prepare a MySQL server for the project:
 -- Creates a database 'hbnb_dev_db'
 -- Creates a new user 'hbnb_dev' in localhost with the password 'hbnb_dev_pwd'
 -- Grants all privileges on 'hbnb_dev_db' to 'hbnb_dev'@'localhost'
 -- Grants SELECT privilege on 'performance_schema' to 'hbnb_dev'@'localhost'
 -- If the database hbnb_dev_db or the user hbnb_dev already exists, the script should not fail

 CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
 CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
 GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
 GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

