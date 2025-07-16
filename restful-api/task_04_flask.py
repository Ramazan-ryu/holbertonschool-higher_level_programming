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



'''
Instructions:
Setting Up Flask:

Install Flask using pip: pip install Flask.
Create a new Python file and import Flask: from flask import Flask.
Instantiate a Flask web server from the Flask module: app = Flask(__name__).
Creating Your First Endpoint:

Define a route for the root URL (“/”) and create a function (def home():) to handle this route. Within the function, return a string: “Welcome to the Flask API!”.
Run the Flask development server with: if __name__ == "__main__": app.run().
Visit http://localhost:5000 in your browser or use curl to see the message.
Serving JSON Data:

Import the jsonify function from Flask: from flask import jsonify.
Create a new route /data and associate a function with it. Inside this function, return a JSON response using jsonify(). This should return a list of all the usernames stored in the API.
Users will be stored in memory using a dictionary with username as the key and the whole object (dictionary) as the value.
Example dictionary: users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
NOTE: To avoid problem with the checker, do not include your testing data when pushing your code.
Expanding Your API:

Add a few more endpoints to simulate different functionalities:
/status: It should return OK.
/users/<username>: Returns the full object corresponding to the provided username. (Hint: Use Flask’s dynamic route feature)
Handling POST Requests:

Import the request object from Flask: from flask import request.
Create a new route /add_user that accepts POST requests.
This route should:
Parse the incoming JSON data. Example data: {"username": "john", "name": "John", "age": 30, "city": "New York"}
Add the new user to the users dictionary using username as the key.
Return a confirmation message with the added user’s data.
Test your code:
Test your application using the flask CLI to run the development server.

$ flask --app task_04_flask.py run
 * Serving Flask app 'task_04_flask.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
Use curl or a python script to test your API.

Hints:
Flask routes are defined using the @app.route() decorator, followed by a function that returns the desired response for that route.
For serving dynamic content in routes, Flask allows you to add variables to the route (e.g., <variable_name>). These can be captured in your function parameters.
The jsonify() function in Flask turns a Python dictionary or list into a response with application/json content-type.
Flask’s development server reloads automatically on code changes. However, for certain types of changes (like adding new files), you might need to restart the server.
Expected Output:
Accessing http://localhost:5000 should show the message: "Welcome to the Flask API!".
Visiting http://localhost:5000/data should return a JSON response with a list of all usernames stored in the API. For example, if the users dictionary contains {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}, the response should be:
["jane", "john"]
The /status endpoint should return the string: "OK".
Accessing /users/jane should return the full object corresponding to the username “jane”. For example:
{
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
}
Similarly, accessing /users/john should return:
{
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
}
But if it doesn’t exist, return {"error": "User not found"}

Posting a new user to /add_user should add the user to the users dictionary and return a 201 status code with a confirmation message with the user’s data. For example, posting:
{
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
}
should return:

{
        "message": "User added",
        "user": {
                "username": "alice",
                "name": "Alice",
                "age": 25,
                "city": "San Francisco"
        }
}
Posting a new user to /add_user without an username should return a 400 code error with the message {"error":"Username is required"}. For example, posting:
{
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
}
should return:

{
        "error": "Username is required"
}
'''
