import http.server
import socketserver
import os

port = 8000
ip = 'localhost'

Handler = http.server.SimpleHTTPRequestHandler

os.chdir(os.path.join(os.path.dirname(__file__),'..','assets',))
with socketserver.TCPServer((ip, port), Handler) as httpd:
    print("serving at port", port)
    httpd.serve_forever()