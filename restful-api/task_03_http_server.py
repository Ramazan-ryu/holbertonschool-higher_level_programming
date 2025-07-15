#!/usr/binpython3
"""Python web server"""

import json
import http.server
import socketserver

PORT=8000

class SimpleAPIHeader(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.response(200)
            self.send_header("Content type", "txt/plain")
            self.end_headers()
            self.wfile.write("Hello. This is the simple API!")
        elif self.data == "/data":
            self.response(200)
            self.send_header("Content type","txt/plain")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dump(data))
        elif self.status == "":
            self.response(200)
            self.send_header("Content type", "txt/plain")
            self.end_headers()
            self.wfile.write("OK")
        elif self.info == "/info":
            self.response(200)
            self.send_header("Content type","txt/plain")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dump(info))
        else:
            self.response(400)
            self.send_header("Content type","txt/plain")
            self.end_headers()
            self.wfile.write("Endpoint not foun")
with socketserver.TCPServer(("",PORT),SimpleAPIHeader) as httpd:
    print("serving port", PORT)
    httpd.serve_forever()
        
