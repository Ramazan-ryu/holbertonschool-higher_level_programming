#!/usr/bin/env python3
#
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API"

@app.route("/data", methods=["GET"])
def data():
    users={
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
    }
    return jsonify(list(users.keys()))

@app.route("/satus", methods=["GET"])
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def users():
    if "username" in users:
        return jsonify()
    else:
        return jsonify({"error": "User not found"})

@app.route("/add_user", methods=["POST"])
def add_user():
    add = request.get_json()
    if not add or "username" not in users:
        return jsonify({"error":"Username is required"}), 400
    else:
        users[username]=add
        return jsonify({"message": "User added", "user": add}), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
