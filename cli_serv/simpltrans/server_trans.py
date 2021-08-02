#!/usr/bin/python3
# -*- coding:utf-8 -*-

import socket

BUFFER_SIZE = 1024

ssFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssFT.bind((socket.gethostname(), 8756))
ssFT.listen(1)

while True:
    (conn, address) = ssFT.accept()
    text_file = 'fileProj.txt'
with open(text_file, 'wb') as fw:
    msg = ssFT.recv(BUFFER_SIZE)
    fsize = int(msg.decode('utf-8'))
    rsize = 0

    while True:
        data = ssFT.recv(BUFFER_SIZE)
        rsize = rsize + len(data)
        fw.write(data)
        if rsize >= fsize:
            print('Breaking from file write')
            break

