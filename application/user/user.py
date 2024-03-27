from flask import Flask, jsonify, render_template, Blueprint
from application.models import User
from application.db import add_user

signin_bp = Blueprint('signin_bp', __name__,template_folder='templates', static_folder='static')

@signin_bp.route('/info/', methods=['POST','GET'])
def info():
    return User().signup()



@signin_bp.route('/', methods=['POST','GET'])
def index():
    return render_template('signup.html')

@signin_bp.route('/signin', methods=['POST','GET'])
def signin():
    return render_template('signup.html')