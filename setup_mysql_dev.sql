import mysql.connector

def prepare_mysql_server():
    try:
        # Establish connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Explanation: Prepare the MySQL server for the project
        # Create the database if it doesn't already exist
        # Create a user and grant privileges on the database
        # Grant select privileges on performance_schema
        # Flush privileges to apply changes
        sql_queries = """
            CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
            CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
            GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
            GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
            FLUSH PRIVILEGES;
        """

        # Execute the SQL statements
        cursor.execute(sql_queries, multi=True)

        # Commit the changes to the database
        connection.commit()

        print("MySQL server prepared successfully.")

    except mysql.connector.Error as error:
        print(f"Error while preparing MySQL server: {error}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Call the function to prepare the MySQL server
prepare_mysql_server()
