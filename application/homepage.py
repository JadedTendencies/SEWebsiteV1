from flask import Blueprint, render_template, redirect, url_for, request

from flask import current_app as app

homepage_bp = Blueprint('homepage', __name__)

@homepage_bp.route('/')
def index():
    return render_template('index.html')

@homepage_bp.route('/about')
def about():
    return render_template('about.html')

# Add more routes and views as needed

app.register_blueprint(homepage_bp)