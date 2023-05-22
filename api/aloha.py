from http.server import BaseHTTPRequestHandler
from urllib import parse
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):
        s = self.path
        print(s)
        url_comp=parse.urlsplit(s)
        query_strings_list = parse.parse_qsl(url_comp.query)
        dic = dict(query_strings_list)
        name = dic.get("name")
        print(name)

        if name:
            message = f"Aloha {name}"
        else:
            message = "Aloha stanger"
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

      
        self.wfile.write(message.encode('utf-8'))
        return