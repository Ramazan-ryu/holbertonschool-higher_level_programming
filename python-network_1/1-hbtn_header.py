#!/usr/bin/python3
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
        with urllib.request.urlopen(url) as zapros:
            head = zapros.headers
            zapros-id-x = headers.get('X-Request-Id')
            print(zapros-id-x)
