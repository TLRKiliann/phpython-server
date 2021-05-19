#!/usr/bin/python3

from socket import *
import time

startTime = time.time()

def launcher():
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)
   
    for i in range(50, 100):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if(conn == 0):
            print ('Port %d : OPEN' % (i,))
            s.close()
    print('Time taken:', time.time() - startTime)

if __name__ == '__main__':
    launcher()