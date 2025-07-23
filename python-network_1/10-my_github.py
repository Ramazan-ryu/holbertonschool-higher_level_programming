#!/usr/bin/python3
"""
This script takes GitHub credentials (username and token)
and uses the GitHub API to display your GitHub user ID.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API endpoint for user info
    url = "https://api.github.com/user"

    # Perform Basic Authentication with username and token
    response = requests.get(url, auth=(username, token))

    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")

"""script that takes your GitHub credentials (username and password) and uses
the GitHub API to display your id

You must use Basic Authentication with a personal access token as password to
access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access token
as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)"""
