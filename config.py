"""Flask App configuration."""
import os
from dotenv import load_dotenv

# Specificy a `.env` file containing key/value config values
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))



class Config:
    """Set Flask config variables."""

    # General Config
    ENVIRONMENT = os.environ.get("ENVIRONMENT")
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_DEBUG = True
    SECRET_KEY = 'dev' #os.environ.get("SECRET_KEY")


    # Database
    MONGO_URI = "mongodb+srv://jadetest:mongodbpassword@cluster0.mqvloxu.mongodb.net/database1" #os.environ.get('MongoDB_DATABASE_URI')


