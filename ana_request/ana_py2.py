#!/usr/bin/python3

from socket import *
import os
import sys
import time

"""
    To open xfce4-terminal (with python) and display netstat -npte (with bash).
"""

os.system("xfce4-terminal -e 'bash -c \"watch -n 1 netstat -npte; exec bash\"'")
startTime = time.time()

def launcher():
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)
    # TCP is'nt assigned for all ports by IANA. let's see :
    # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
    for i in range(37, 100):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if(conn == 0):
            print ('Port %d : OPEN' % (i,))
            s.close()
    print('Time taken:', time.time() - startTime)

if __name__ == '__main__':
    launcher()
