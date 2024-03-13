import os

from flask import Flask, render_template
from application.user.user import signin_bp
from application.homepage.homepage import homepage_bp



# creating the factory

def create_app():
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(APP_DIR, 'build/static')
    TEMPLATE_FOLDER = os.path.join(APP_DIR, 'build/templates')
    app = Flask(__name__, static_folder=None, template_folder=None, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        app.register_blueprint(homepage_bp, url_prefix='')
        app.register_blueprint(signin_bp, url_prefix='/user')

    return app