#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You dont need to check arguments passed to the script (number or type)
Please test your script in the container provided, using the web server running on port 5000
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
