#!/usr/bin/python3
"""simple API using python with flask"""

from flask import Flask
from flask import jsonify
from flask import request

usernames = {}

app = Flask(__name__)


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/data")
def get_data():
    return jsonify(list(usernames.keys()))


@app.route("/status")
def get_status():
    return ("OK")


@app.route("/users/<username>")
def get_user(username):
    user = usernames.get(username)
    if username in usernames:
        return jsonify(user)
    else:
        return jsonify({"error": "User was not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    usernames[username] = data
    return jsonify({"message": "User added successfully", "user": data}), 201


if __name__ == "__main__":
    app.run()
