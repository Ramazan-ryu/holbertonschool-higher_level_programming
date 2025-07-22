#! /usr/bin/env python3
"""This script fetches data from
    https://alx-intranet.hbtn.io/status
"""

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    data = response.read()
    print("Body response")
    print("".format(type(body)))
    print("".format(body))
    print("".format(body.decode('utf-8')))
