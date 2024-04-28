from flask import Flask, jsonify, render_template, Blueprint

homepage_bp = Blueprint('homepage_bp', __name__, static_folder='static', static_url_path='/homepage/static', template_folder='templates')

@homepage_bp.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')



@homepage_bp.route('/about', methods=['POST','GET'])
def about():
    return render_template('about.html')

