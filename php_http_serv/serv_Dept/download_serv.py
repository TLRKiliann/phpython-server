#!/usr/bin/python3
# -*- coding: utf-8 -*-

__SERVER1__="""
#################################

            SERVER 1
       (127.0.0.1:8000)

#################################
"""

"""
    Happy server and play with them !
    To upload file test.txt, proceed as next :
    $ python3 download_serv.py
    In an other shell :
    sudo php -S 127.0.0.1:6688
    Run your browser :
    $ firefox &
    Entrer : 127.0.0.1:6688
    Press : Browse
    Then press : Download
    New window appear to show you content of 
    test.txt on server launched by 
    download_serv.py ($ python3 download_serv.py)
    (127.0.0.1:8000)
"""

import http.server # Our http server handler for http requests
import socketserver # Establish the TCP Socket connections

print(__SERVER1__)

PORT = 8000
 
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Name of file to download
        self.path = 'test.txt'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
 
Handler = MyHttpRequestHandler
 
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port :", PORT)
    print("Ready and waiting connection...")
    httpd.serve_forever()
