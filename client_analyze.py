#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket()

ip = input("Enter IP addr (target): ")
port = str(input("Enter PORT of target: "))

s.connect((ip, int(port)))

print(s.recv(1024))
