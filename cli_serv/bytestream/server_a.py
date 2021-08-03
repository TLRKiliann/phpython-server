#!/usr/bin/python3

import socket
import pickle

__introserv__="""
--------------------------------
    Bytestream transfert !
--------------------------------
"""

print(__introserv__)

HEADERSIZE = 10

# No good socket for sending memoryview !!!
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)
print("[+] Waiting connection from client...")

while True:
    clientsocket, address = s.accept()
    print(f"[+] Connection from {address} has been established !")
    
    d = {1 : "Hey", 2 : "Goood"}
    msg = pickle.dumps(d)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket.send(msg)

    outgo = input("[+] Continue ? (y/n): ")
    if outgo == "n":
        print("[+] Connection finished...")
        break
    else:
        print("-.- Continue -.-")