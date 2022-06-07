import http.server
import socketserver
import os

IP = "localhost"
PORT = 8000
DIRECTORY = f"{os.getcwd()}/html"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_host():
    http = socketserver.TCPServer((IP, PORT), Handler)
    print(f"Started HTML Web Server at http://localhost:8000")
    http.serve_forever()

start_host()