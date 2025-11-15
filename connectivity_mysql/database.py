

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",       # XAMPP default: empty password
      # optional
)

print("Connected:", mydb.is_connected())

