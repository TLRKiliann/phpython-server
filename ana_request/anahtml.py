#!/usr/bin/python3
# -*- coding:utf-8 -*-


__HTMLCOPY__="""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

      This script retrive html code
      from a site to copy all data into
      file_html.txt
      Easy to get that with *http.server*

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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

class ServerHtml(BaseHTTPRequestHandler):
    def do_GET(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        ask_addr = input("Enter address plz : https://www.")
        url = "https://www." + ask_addr
        rg = requests.get(url, data=payload)
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
        with open("file_html.txt", 'w+b') as fileh:
            fileh.write(bytes(rg.content))

if __name__ == "__main__":
    webServer = HTTPServer((host, port), ServerHtml)
    print("Server started http://%s:%s" % (host, port))
    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
