#!/usr/bin/python3

import socket
import time

TCP_IP = 'localhost'
TCP_PORT = 5000

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((TCP_IP, TCP_PORT))
recived_f = 'myfile' + str(time.time()).split('.')[0] + '.txt'
with open(recived_f, 'wb') as f:
    print('file opened')
    while True:
        #print('receiving data...')
        data = socket_client.recv(1024)
        print('data=%s', (data))
        if not data:
            f.close()
            print('file close()')
            break
        # write data to a file
        f.write(data)

print('Successfully get the file !')
socket_client.close()
print('-- Connection closed --')
