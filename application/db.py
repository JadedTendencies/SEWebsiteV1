import bson
from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from flask_login import UserMixin

# DB Setup
def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
    return db

db = LocalProxy(get_db)

# User Model adapted for Flask-Login
class User(UserMixin):
    def __init__(self, user_doc):
        self._id = user_doc['_id']
        self.first_name = user_doc['First Name']
        self.last_name = user_doc['Last Name']
        self.email = user_doc['Email']
        self.password = user_doc['Password']

    def get_id(self):
        """
        Override the method to return the MongoDB user ID as a string.
        This is necessary because Flask-Login expects the user ID to be unicode or string.
        """
        return str(self._id)

# Function to help in user loading by Flask-Login
def load_user(user_id):
    user_doc = db.UserInfoTest.find_one({"_id": ObjectId(user_id)})
    return User(user_doc) if user_doc else None

# Models
class Add_User:
    def signup(self, first_name, last_name, email, password):
        user = {
            "First Name": first_name,
            "Last Name": last_name,
            "Email": email,
            "Password": password
        }
      ##  print("Attempting to insert user:", user)  # Before insertion
        result = db.UserInfoTest.insert_one(user)
      ##  print("Insertion result:", result.inserted_id)  # After insertion
        return result.inserted_id

def authenticate_login(email=None, user_id=None):
    user_doc = None
    if user_id is not None:
        try:
            user_doc = db.UserInfoTest.find_one({"_id": ObjectId(user_id)})
        except InvalidId:
            return None
    elif email is not None:
        user_doc = db.UserInfoTest.find_one({"Email": email})
    
    return User(user_doc) if user_doc else None
