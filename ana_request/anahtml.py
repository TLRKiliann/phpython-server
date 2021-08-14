#!/usr/bin/python3
# -*- coding:utf-8 -*-


__HTMLCOPY__="""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

      This script html code
      from the site to html_copy.txt 

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""


import os
import http.server
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import requests
import requests_raw
import binascii


print(__HTMLCOPY__)

port = 6059
host = "127.0.0.1"
run_fire = host +":"+ str(port)
os.system("xfce4-terminal -e 'bash -c \"firefox {}; exec bash\"'".format(run_fire))

class RetrieverHtml(BaseHTTPRequestHandler):
    def do_GET(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        url = "https://www.myip.com/"
        #rg = requests.get("https://www.myip.com/")
        rg = requests.get('https://www.myip.com/', data=payload)
        print("[+] Status :", rg.status_code)
        print("\n")
        print("[+] Requests URL : ", rg.url)
        print("\n")
        rg.content
        print("[+] Requests content : ")
        print(type(rg.content))
        print("[+] Requests content [0:600] : ")
        print(rg.content[0:600])
        print("\n")
        self.wfile.write(bytes("<p> --- Content : </p>", "utf-8"))
        self.wfile.write(bytes(rg.content))

if __name__ == "__main__":
    webServer = HTTPServer((host, port), RetrieverHtml)
    print("Server started http://%s:%s" % (host, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
