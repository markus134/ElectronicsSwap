import mysql.connector

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    auth_plugin='mysql_native_password'
)

# Create a cursor to execute SQL commands
my_cursor = mydb.cursor()

# Create the "users" database if it doesn't exist
my_cursor.execute("CREATE DATABASE IF NOT EXISTS users")

# Select the "users" database
my_cursor.execute("USE users")

# Define the table structure with the desired columns
create_table_query = """
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    email VARCHAR(150) NOT NULL,
    password VARCHAR(150) NOT NULL
)
"""

my_cursor.execute(create_table_query)
