#!/usr/bin/python3
#! -*- coding : utf-8 -*-


__RdProc__ = """
¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢

      !!! To launch PHP SERVER !!!

At the first launch of the php server, you 
have to enter a password for the superuser, 
which interrupts the program.
You just have to restart programm with the 
following command :
> python3 ana_html.py

¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢
"""


import os
import sys
import socket
import hey_bro


def callProcFunc(servphp, url):
    print(__RdProc__)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 80))
    if result == 0:
       print("Port of php server - open")
       # To call hey_bro.py for launching function callMyBrow(url) :
       hey_bro.callMyBrow(url)
    else:
       print("php server - close")
       os.system("xfce4-terminal -e 'bash -c \"{}; exec bash\"'".format(servphp))
