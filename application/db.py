import bson

from flask import current_app, g, jsonify
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

# DB SETUP

def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:

        db = g._database = PyMongo(current_app).db
       
    return db


db = LocalProxy(get_db)

# MODELS

class Add_User:
    def signup(self, first_name, last_name, email, password):
        user = {
            "First Name": f"{first_name}",
            "Last Name": f"{last_name}",
            "Email": f"{email}",
            "Password": f"{password}"
        }
        db.UserInfoTest.insert_one(user)
        return 200
