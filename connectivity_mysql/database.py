import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",       # XAMPP default: empty password
      # optional
)

print("Connected:", mydb.is_connected())

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS school")
print("Database created successfully.")

