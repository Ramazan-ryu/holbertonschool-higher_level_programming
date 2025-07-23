#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays 
the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    """Ensure the code is executed when direclty run"""
    er = sys.argv[1]
    req = request.Request(er)
    req.add_header("cfclearance", 'true')

    try:
        with request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print("Error code:", e.code)
