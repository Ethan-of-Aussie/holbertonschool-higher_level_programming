#!/usr/bin/python3


import http.server
import json

class httpsub(http.server.BaseHTTPRequestHandler):


    def do_GET(self):
        try:
            if self.path == "/data":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                data = {"name": "John", "age": 30, "city": "New York"}
                self.wfile.write(json.dumps(data).encode())
                return

            if self.path == "/status":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"status": "OK"}')
                return

            if self.path == "/":
                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Hello, this is a simple API!")
                return
            if self.path == "/info":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                info = {"version": "1.0", "description": "A simple API built with http.server"}
                self.wfile.write(json.dumps(info).encode())
                return
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"server error: {e}".encode())

host = 'localhost'
port = 8000
http.server.HTTPServer((host, port), httpsub).serve_forever()
