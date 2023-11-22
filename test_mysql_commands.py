#!/usr/bin/python3
import unittest
import MySQLdb

class TestMySQLCommands(unittest.TestCase):

    def setUp(self):
        # Connect to the MySQL database
        self.db = MySQLdb.connect(
            host='your_host',  # Replace with your MySQL server hostname or IP address
            user='your_username',  # Replace with your MySQL username
            passwd='your_password',  # Replace with your MySQL password
            db='your_database'  # Replace with your database name
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Close the database connection after the test
        self.db.close()

    def test_create_command(self):
        # Get the number of current records in the table 'states'
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Execute the console command (for example: create State name="California")
        # Assuming your command is executed through another part of your code,
        # you might need to emulate that process here or directly execute the SQL command.

        # After executing the command, get the number of records again
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        # Check if the difference in record count is +1
        self.assertEqual(final_count - initial_count, 1, "New record not added successfully")
