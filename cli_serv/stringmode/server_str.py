#!/usr/bin/python3
# -*- coding:utf-8 -*-

__TCPMSG__="""
--------------------------------
    TCP is bi-directional
--------------------------------
"""

import socket
import sys

print(__TCPMSG__)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 10000)
print(sys.stderr, "[+] Starting on %s port %s" % server_address)
sock.bind(server_address)

sock.listen(5)

while True:
    print(sys.stderr, "[+] Waiting for connection...")
    connection, client_address = sock.accept()

    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(sys.stderr, 'received "%s"' % data)
            if data:
                print(sys.stderr, 'sending data back to the client')
                connection.sendall(data)
            else:
                print(sys.stderr, 'no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()
