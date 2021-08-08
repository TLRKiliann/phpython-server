#!/usr/bin/python3
# -*- coding:utf-8 -*-


__TOUSE__="""
------------------------------------------

    Client receive msg from server !

------------------------------------------
"""


import socket                   # Import socket module


print(__TOUSE__)

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send(b"Hello server!")

with open('received_file', 'wb') as f:
    print("[+] File opened...")
    while True:
        data = s.recv(1024)
        if not data :
            print("[+] Finish !!!")
            break
        else:
            print("[+] Receiving data...")
            print("[!] data=%s", bytes(data))
        #if not data:
        #break
        # write data to a file
        f.write(data)

f.close()
print("[+] Successfully get file !")
s.close()
print("[!] Connection closed !")

