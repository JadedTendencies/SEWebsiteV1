import os

from flask import Flask, render_template
from application.sign_in.signin import signin_bp



# creating the factory

def create_app():
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(APP_DIR, 'build/static')
    TEMPLATE_FOLDER = os.path.join(APP_DIR, 'build/templates')
    app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder= TEMPLATE_FOLDER, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        app.register_blueprint(signin_bp)

        @app.route('/')
        def index():
            return render_template('index.html')
    
        @app.route('/about/')
        def about():
            return render_template('about.html')
    
    return app