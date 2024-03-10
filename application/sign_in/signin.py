from flask import Flask, jsonify, render_template, Blueprint
from application.models import User

signin_bp = Blueprint('signin', __name__)

@signin_bp.route('/user/signup/', methods=['POST','GET'])
def signup():
    return User().signup()



@signin_bp.route('/signup/', methods=['POST','GET'])
def index():
    return render_template('signup.html')

