from http.server import BaseHTTPRequestHandler
import subprocess

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        response = subprocess.check_output(['python', 'main.py', body]).decode('utf-8')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
