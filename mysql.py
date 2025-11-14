import mysql.connector
from mysql.connector import Error

try:
    # Establish connection
    connection = mysql.connector.connect(
        host='localhost',      # your host, e.g., 'localhost'
        user='your_username',  # your MySQL username
        password='your_password',  # your MySQL password
        database='your_database'   # name of the database
    )

    if connection.is_connected():
        print("✅ Successfully connected to MySQL database")

        # Create a cursor object
        cursor = connection.cursor()

        # Example: Create a table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                email VARCHAR(50)
            )
        """)

        # Example: Insert data
        cursor.execute("""
            INSERT INTO users (name, email) VALUES (%s, %s)
        """, ("Alice", "alice@example.com"))
        connection.commit()
        print("Data inserted successfully")

        # Example: Query data
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except Error as e:
    print(f"❌ Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
