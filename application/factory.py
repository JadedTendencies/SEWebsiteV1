import os

from flask import Flask
import dotenv



def create_app():
    
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(APP_DIR, 'build/static')
    TEMPLATE_FOLDER = os.path.join(APP_DIR, 'build/templates')

    app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder= TEMPLATE_FOLDER, instance_relative_config=False)
    app.config.from_object('config.Config')




    return app