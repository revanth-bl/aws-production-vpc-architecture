from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = """
        <html>
        <head><title>AWS VPC Project</title></head>
        <body>
        <h1>🚀 AWS Production VPC Architecture Deployed Successfully</h1>
        <p>Running inside Private EC2 via Auto Scaling Group</p>
        </body>
        </html>
        """
        self.wfile.write(message.encode())

server = HTTPServer(('0.0.0.0', 80), Handler)
print("Server running on port 80...")
server.serve_forever()