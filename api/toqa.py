from http.server import BaseHTTPRequestHandler
from urllib import parse
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):
        s = self.path
        print(s)
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        message = "Welcome Toqa ^_^"
        self.wfile.write(message.encode('utf-8'))
        return