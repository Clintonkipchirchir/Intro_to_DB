import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",   
    user="root",
    password="@Terminal254"
)

cursor = mydb.cursor()

try:
    cursor.execute("CREATE DATABASE alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except Exception as e:
    print("Database 'alx_book_store' already exists!")
else:
    mydb.close()

