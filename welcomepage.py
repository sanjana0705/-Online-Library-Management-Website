import mysql.connector
import hashlib
from getpass import getpass

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change to your MySQL username
    password="Root",  # Change to your MySQL password
    database="library_db"
)

cursor = db.cursor()

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    password = getpass("Enter a new password: ")

    hashed_password = hash_password(password)  # Hash the password

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        print("\nRegistration successful! You can now log in.\n")
    except mysql.connector.IntegrityError:
        print("\nUsername already exists. Try again.\n")
    
    login()

# Function to authenticate user
def login():
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    hashed_password = hash_password(password)  # Hash the entered password

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
    user = cursor.fetchone()

    if user:
        print("\nLogin successful! Redirecting to dashboard...\n")
        dashboard(username)
    else:
        print("\nInvalid username or password. Try again.\n")
        login()

# Function to display the dashboard
def dashboard(username):
    print(f"Welcome to the dashboard, {username}!")
    print("1. Logout")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        logout()
    else:
        print("Invalid choice, returning to dashboard...\n")
        dashboard(username)

# Function to logout
def logout():
    print("\nLogged out successfully!\n")
    login()

# Start the program
print("1. Register\n2. Login")
choice = input("Enter your choice: ")
if choice == "1":
    register()
elif choice == "2":
    login()
else:
    print("Invalid choice, exiting...")
