#!/usr/bin/python3
"""This script fetches data from
    https://alx-intranet.hbtn.io/status
"""

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    data = response.read()
    print("Body response")
    print("- type:".format(type(body)))
    print("- content:".format(body))
    print("- utf8 content:".format(body.decode('utf-8')))
