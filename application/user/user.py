from flask import Flask, jsonify, render_template, Blueprint, request, g, redirect
from application.db import Add_User

signin_bp = Blueprint('signin_bp', __name__,template_folder='templates', static_folder='static')


@signin_bp.route('/info', methods=['POST','GET'])
def info():
    if request.method == 'POST':
        new_user = Add_User().signup(request.form['first-name'], request.form['last-name'],request.form['email'],request.form['password'])
    return redirect('/')



@signin_bp.route('/', methods=['POST','GET'])
def index():
    return render_template('signup.html')

@signin_bp.route('/signin', methods=['POST','GET'])
def signin():
    return render_template('signup.html')