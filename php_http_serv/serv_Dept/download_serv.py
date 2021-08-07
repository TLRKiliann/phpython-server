#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Server downloader !!!
    To upload file index.php,
    launch index.php at first.
    Use this command :
    sudo php -S 127.0.0.1:8000
    and then run python3 download_serv.py
"""

import http.server # Our http server handler for http requests
import socketserver # Establish the TCP Socket connections
 
PORT = 8000
 
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'index.php'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
 
Handler = MyHttpRequestHandler
 
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()
