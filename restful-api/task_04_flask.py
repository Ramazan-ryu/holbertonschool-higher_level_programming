#!/usr/bin/env python3
#
from flask import jsonify
from flask import request
from flask import Flask

app = Flask(__name__)
users={}

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    add = request.get_json()
    if not add or "username" not in add:
        return jsonify({"error":"Username is required"}), 400    
    username = add["username"]
    users[username]=add
    return jsonify({"message": "User added", "user": add}), 201



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
