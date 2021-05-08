#!/usr/bin/python3
# -*- coding: utf-8 -*-


import http.server
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import requests
import time

host = "localhost"
port = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        url = 'https://collonges.gammadia-dsi.net/_/login'
        rg = requests.get('https://collonges.gammadia-dsi.net/_/login', data=payload)
        print("Status :", rg.status_code)
        print(rg.raw)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        #self.wfile.write(bytes("<html><head><title>https://my_server2_to_test.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s </p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is web server 2.</p>", "utf-8"))
        self.wfile.write(bytes("<br> ---GET URL : ", "utf-8"))
        self.wfile.write(bytes(rg.url, "utf-8"))
        self.wfile.write(bytes("<br> ---GET + Headers-Content-Type : ", "utf-8"))
        self.wfile.write(bytes(rg.headers['content-type'], "utf-8"))
        self.wfile.write(bytes("<br> ---Encoding : ", "utf-8"))
        self.wfile.write(bytes(rg.encoding, "utf-8"))
        self.wfile.write(bytes("<br> ---Text data : ", "utf-8"))
        self.wfile.write(bytes(rg.text, "utf-8"))
        self.wfile.write(bytes(rg.content))
        self.wfile.write(bytes("<br> ---Raw : <br>", "utf-8"))
        self.wfile.write(bytes(rg.raw))
        self.wfile.write(bytes("<br> ---GET finished--- <br>", "utf-8"))
        self.wfile.write(bytes("------------- <br>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((host, port), MyServer)
    print("Server started http://%s:%s" % (host, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
