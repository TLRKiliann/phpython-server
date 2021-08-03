#!/usr/bin/python3

import socket
import pickle

__introcli__="""
--------------------------------
    Bytestream transfert !
--------------------------------
"""

print(__introcli__)

HEADERSIZE = 10

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((socket.gethostname(), 1235))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = socket_client.recv(16)
        if new_msg:
            print(f"[+] New message length : {msg[:HEADERSIZE]}")
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE == msg_len:
            print("[+] Full msg recvd !")
            print(full_msg[HEADERSIZE:])
            
            data = pickle.loads(full_msg[HEADERSIZE:])
            print(data)
            new_msg = True
            full_msg = b''
            break
    print(full_msg)
    socket_client.close()
    print("[+] Transfert bytestream finished !")
    break
