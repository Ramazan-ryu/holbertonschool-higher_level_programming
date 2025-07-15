#!/usr/bin/env python3
"""Python web server"""

import json
import http.server
import socketserver

PORT=8000

class SimpleAPIHeader(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "txt/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple AP")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type","txt/plain")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "txt/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type","txt/plain")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type","txt/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

with socketserver.TCPServer(("",PORT),SimpleAPIHeader) as httpd:
    print(f"serving port {PORT}")
    httpd.serve_forever()
