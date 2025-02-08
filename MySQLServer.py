import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",   
    user="root",
    password="@Terminal254"
)

cursor = mydb.cursor()

try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))

else:
    mydb.close()

