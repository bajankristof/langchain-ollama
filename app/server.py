import json

from http.server import BaseHTTPRequestHandler, HTTPServer

from .llm import llm

class LLMHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

    def do_GET(self):
        content_length = int(self.headers.get('Content-Length'))
        prompt = self.rfile.read(content_length).decode("utf-8")
        response = llm.invoke(prompt)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response.dict()).encode())

def serve():
    server = HTTPServer(('', 8080), LLMHandler)
    server.serve_forever()
