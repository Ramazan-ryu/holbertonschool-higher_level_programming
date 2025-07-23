#!/usr/bin/python3
"""This script fetches data from
https://alx-intranet.hbtn.io/status
"""
from urllib import request
if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    try:
        with urllib.request.urlopen(url) as zapros:
            body = zapros.read()
            print("Body response")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except Exception as e:
        print(f"Error ocuured as {e}")
