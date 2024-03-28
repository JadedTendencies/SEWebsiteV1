from flask import Flask, url_for, render_template, Blueprint, request, g, redirect, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from application.db import Add_User, authenticate_login

signin_bp = Blueprint('signin_bp', __name__,template_folder='templates', static_folder='static')


@signin_bp.route('/info', methods=['POST','GET'])
def info():
    if request.method == 'POST':
        new_user = Add_User().signup(request.form['first-name'], request.form['last-name'],request.form['email'],request.form['password'])
    return redirect('/')



@signin_bp.route('/', methods=['POST','GET'])
def test():
    return render_template('signup.html')

@signin_bp.route('/signup', methods=['POST','GET'])
def signup():
    return render_template('signup.html')

@signin_bp.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None
        user = authenticate_login(email)

        if user is None:
            error = 'Incorrect username.'
        elif not user['Password'] == password:
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = str(user['_id'])
            session['first_name'] = user['First Name']
            return redirect(url_for('signup'))

        flash(error)


    return render_template('login.html')

@signin_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = authenticate_login(None, id=user_id)