

#abhi
'''from flask import Flask, render_template, request, redirect, session, jsonify, url_for
import mysql.connector
from flask_bcrypt import Bcrypt
import logging

# Initialize Flask App
app = Flask(__name__, template_folder="templates")
app.secret_key = 'your_secret_key'  # Use a secure key

bcrypt = Bcrypt(app)

# Logging Configuration
logging.basicConfig(level=logging.INFO)

# MySQL Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root",
        database="library_db"
    )

# ---------------- ROUTES ----------------

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# ----------- USER ROUTES -----------

# User Signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        mobile = request.form['mobile']
        email = request.form['email']
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        try:
            db = get_db_connection()
            cursor = db.cursor()

            cursor.execute("""
                INSERT INTO users (fullname, mobile, email, username, password, role)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (fullname, mobile, email, username, password, 'user'))

            db.commit()
            return redirect(url_for('home'))

        except mysql.connector.IntegrityError as e:
            logging.error("Signup Error: %s", e)
            return jsonify({"error": "Username or Email already exists!"}), 400

        finally:
            cursor.close()
            db.close()

    return render_template('signup.html')

# ----------- ADMIN ROUTES -----------

# Admin Signup
@app.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        try:
            db = get_db_connection()
            cursor = db.cursor()

            cursor.execute("""
                INSERT INTO users (fullname, email, username, password, role)
                VALUES (%s, %s, %s, %s, %s)
            """, (fullname, email, username, password, 'admin'))

            db.commit()
            return redirect(url_for('home'))

        except mysql.connector.IntegrityError as e:
            logging.error("Admin Signup Error: %s", e)
            return jsonify({"error": "Username or Email already exists!"}), 400

        finally:
            cursor.close()
            db.close()

    return render_template('admin_register.html')

# ----------- COMMON LOGIN -----------

# User/Admin Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT id, username, password, role FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            session.permanent = True

            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('user_book_page'))

        return jsonify({"error": "Invalid username or password!"}), 401

    finally:
        cursor.close()
        db.close()

# ----------- DASHBOARD ROUTES -----------

# first User Book Page
@app.route('/book_page')
def user_book_page():
    if 'user_id' in session and session.get('role') == 'user':
        return render_template('book.html', username=session['username'])
    return redirect(url_for('home'))

# Admin Dashboard
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'user_id' in session and session.get('role') == 'admin':
        return render_template('admin_dashboard.html', username=session['username'])
    return redirect(url_for('home'))

# ----------- LOGOUT -----------

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# ----------- RUN APP -----------

if __name__ == '__main__':
    app.run(debug=True)'''
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# User Book Page (After User Login)
@app.route('/book')
def user_book_page():
    return render_template('book.html')

# User Dashboard Page
@app.route('/user/dashboard')
def user_dashboard():
    return render_template('dashboard.html')

# User Profile Page
@app.route('/user/profile')
def user_profile():
    return render_template('profile.html')

# Issue Book Page (User Request Books)
@app.route('/issue_book')
def issue_book():
    return render_template('issue_book.html')

# Admin Dashboard (After Admin Login)
@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Logout (Redirect to Login Page)
@app.route('/logout')
def logout():
    return redirect(url_for('login'))

#borrow page
@app.route('/borrow')
def borrow_page():
    return render_template('borrow.html')


# Login Route (Handles Admin and User Login)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin123':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('user_book_page'))
    return render_template('index.html')

#admin
@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        phone_number = request.form['phone_number']
        password = request.form['password']
        
        if not (full_name and username and phone_number and password):
            return "Missing form data", 400

        # Example of saving admin to the database (adjust for your schema)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO admin (full_name, username, phone_number, password) VALUES (%s, %s, %s, %s)",
                       (full_name, username, phone_number, password))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('admin_login'))  # Redirect to admin login after registration

    return render_template('admin_register.html')

#payment
@app.route('/payment/<int:book_id>')
def payment_page(book_id):
    # Fetch book details (for display) from localStorage or database if needed
   # print(f"Received book_id: {book_id}")  # Debugging Output
    return render_template('payment.html', book_id=book_id)

if __name__ == '__main__':
    app.run(debug=True)
