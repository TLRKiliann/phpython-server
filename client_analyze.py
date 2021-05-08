#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket()

ip = input("Plz enter IP addr (target): ")
port = str(input("Plz enter the port of target: "))

s.connect((ip, int(port)))

print(s.recv(1024))
