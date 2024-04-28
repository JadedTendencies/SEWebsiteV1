from flask import Blueprint, render_template, request, redirect, url_for, flash, g
from flask_login import login_user, logout_user, login_required, current_user
from application.db import authenticate_login, Add_User

signin_bp = Blueprint('signin_bp', __name__, template_folder='templates', static_folder='static')

# Route for user information (Assuming it's for logged-in users)
@signin_bp.route('/info', methods=['POST', 'GET'])
@login_required
def info():
    # Example content, adjust according to your application's context
    return render_template('user_info.html', user=current_user)

# User registration
@signin_bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
        password = request.form['password']  # Remember, no password hashing yet
       
        print("Received signup form data:", first_name, last_name, email, password)  # Print form data

        new_user = Add_User().signup(first_name, last_name, email, password)
       
        print("New user ID:", new_user)  # Print the new user's ID

        if new_user:
            # Auto login after register or redirect to login page
            return redirect(url_for('signin_bp.login'))
        else:
            flash("Signup failed, please try again.")

    return render_template('signup.html')

# Login route
@signin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']  # Again, assuming plaintext for now
        user = authenticate_login(email=email)

        if user and user.password == password:
            login_user(user)
            return redirect(url_for('signin_bp.info'))  # Redirecting to the info page as an example
        else:
            flash('Invalid username or password')

    return render_template('login.html')

# Logout route
@signin_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage_bp.index'))  # Make sure to adjust this to your homepage route
