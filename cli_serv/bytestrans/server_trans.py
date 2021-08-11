#!/usr/bin/python3
# -*- coding:utf-8 -*-


__TOSERV__="""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    Run client_trans.py in an other shell !

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""


import socket
import os


print(__TOSERV__)

port = 60000
s = socket.socket()
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print("[+] Server waiting connection...")

while True:
    clientsocket, addr = s.accept()     # Establish connection with client.
    print("[+] Got connection from", addr)
    data = clientsocket.recv(1024)
    print("[!] Server received :", bytes(data))

    filename = 'mytext'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       clientsocket.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('[+] Done sending')
    clientsocket.send(b"Thank you for connecting")
    clientsocket.shutdown(60)
    clientsocket.close()
