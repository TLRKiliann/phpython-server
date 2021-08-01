#!/usr/bin/python3

import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))

while True:
    full_msg = ""
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"New message length : {msg[:HEADERSIZE]}")
            msg_len = bytes(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")
        if len(full_msg)-HEADERSIZE == msg_len:
            print("Full msg recvd !")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ""
    print(full_msg)
