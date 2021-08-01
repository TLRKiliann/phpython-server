#!/usr/bin/python3

import socket
import time

HEADERSIZE = 10

# No good socket for sending memoryview !!!
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address= s.accept()
    print(f"Connection from {address} has been established !")

    msg = "Wellcome to the server"
    msg = f"{len(msg):<{HEADERSIZE}}" + msg

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        #time.sleep(3)
        #msg = f"Time is : {date.time()}"
        data = b"a" #* (1024 * 100000)
        mv = memoryview(data)
        #sent = s.send(mv)
        #mv = mv[sent:]
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        clientsocket.send(bytes(msg, "utf-8"))
        sent = clientsocket.send(mv)
        mv = mv[sent:]
