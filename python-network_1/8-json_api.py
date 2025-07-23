#!/usr/bin/python3
"""This script sends a POST request with a search letter
and processes the JSON response."""

import requests
import sys

# Get the letter (if given)
if len(sys.argv) > 1:
    q = sys.argv[1]  # Take the first argument
else:
    q = ""           # If nothing is given, use empty string

# Prepare the POST request
url = "http://0.0.0.0:5000/search_user"
data = {'q': q}

# Send the POST request and get the response
response = requests.post(url, data=data)

# Try to convert the response to JSON
try:
    json_data = response.json()
    if json_data:
        print(f"[{json_data.get('id')}] {json_data.get('name')}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
