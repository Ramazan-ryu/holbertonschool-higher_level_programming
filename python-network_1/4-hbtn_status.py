#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following
example (tabulation before -)
"""

import requests
if __name__ == "__main__":
    url = requests.get('https://intranet.hbtn.io/status')
    body = url.txt
    print("Body response")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
