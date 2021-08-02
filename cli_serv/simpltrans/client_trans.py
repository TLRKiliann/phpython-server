#!/usr/bin/python3
# -*- coding:utf-8 -*-

import socket
import os

BUFFER_SIZE = 1024

csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csFT.connect((socket.gethostname(), 8756))

text_file = 'passphrase.txt'

fsize = os.path.getsize(text_file)
csFT.send(str(fsize).encode('utf-8'))

with open(text_file, 'rb') as fs:
    data = fs.read(BUFFER_SIZE)
    while data:
        csFT.send(data)
        data = fs.read(BUFFER_SIZE)
