#!/usr/bin/python3
"""This script fetches data from https://alx-intranet.hbtn.io/status
"""

from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as response:
    data = response.read()
    print("Body response")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
