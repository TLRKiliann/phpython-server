#!/usr/bin/python3

import socket
import time

TCP_IP = 'localhost'
TCP_PORT = 5000

def client_receiver():
    # socket.AF_INET = IPv4 and socket.SOCK_STREAM = TCP
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((TCP_IP, TCP_PORT))

    recived_f = 'myfile' + str(time.time()).split('.')[0] + '.txt'
    with open(recived_f, 'wb') as f:
        print('file opened')
        #print('receiving data...')
        data = socket_client.recv(1024)
        print('data=%s', (data))
        if not data:
            f.close()
            print('file close()')
        else:
            # write data to a file
            f.write(data)
            print('Successfully get the file !')
            socket_client.close()
            print('-- Connection closed --')

if __name__=='__main__':
    order = input("Would you like to download file ? (y/n): ")
    if order == 'y':
        client_receiver()
    else:
        print('-- Connection closed --')
