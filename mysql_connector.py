import mysql.connector

# Connect to MySQL Workbench
'''db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="Root",  # Replace with your MySQL password
    database="library_db"  # Replace with your database name
)

if db.is_connected():
    print("Connected to MySQL successfully!")
else:
    print("Failed to connect.")
'''
conn=mysql.connector.connect(host='localhost',username='root',password='Root',database='library_db')
my_cursor=conn.cursor()
conn.commit()
conn.close()

print("Connected to MySQL successfully!")