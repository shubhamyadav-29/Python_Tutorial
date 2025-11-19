import mysql.connector

db = mysql.connector.connect(
    user="root",
    host="localhost",
    password="chandanray"
)

cursor=db.cursor()

cursor.execute("CREATE DATABASE  IF NOT EXISTS shubham")
print("Database create successfully")
