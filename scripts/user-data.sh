#!/bin/bash

yum update -y
yum install -y python3

cd /home/ec2-user

cat <<EOF > app.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = """
        <html>
        <h1>AWS Production VPC Running</h1>
        </html>
        """
        self.wfile.write(message.encode())

server = HTTPServer(('0.0.0.0', 80), Handler)
server.serve_forever()
EOF

nohup python3 app.py > app.log 2>&1 &