from flask import Flask, jsonify

class User:
    def signup(self):
        user = {
            "First Name": "",
            "Last Name": "",
            "Email": "",
            "Password": ""
        }

        return jsonify(user), 200
