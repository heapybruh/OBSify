import http.server
import socketserver
import os
import json

config_json = open("webserver_config.json", "r", encoding="utf-8")
config = json.loads(config_json.read())

IP = "localhost"
if isinstance(config["Port"], int) == "False":
    PORT = 8000
else:
    PORT = config["Port"]
DIRECTORY = f"{os.getcwd()}/html"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_host():
    http = socketserver.TCPServer((IP, PORT), Handler)
    print(f"Started HTML Web Server at http://localhost:8000")
    http.serve_forever()

start_host()