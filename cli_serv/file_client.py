#!/usr/bin/python3


import socket
import time


TCP_IP = socket.gethostbyname("127.0.0.1")
TCP_PORT = 5000

def client_receiver():
    # socket.AF_INET = IPv4
    # socket.SOCK_STREAM = TCP
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((TCP_IP, TCP_PORT))
    socket_client.send(b"Hello server !")

    recived_f = 'fileX.txt'
    with open('received_file', 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            # Some trbl here !!!
            data = socket_client.recv(1024)
            print('data=%b', (data))
            if not data:
                break
            # write data to a file
            f.write(data)
            f.close()
            print('Successfully get the file')
            socket_client.close()
            print('connection closed')

if __name__=='__main__':
    order = input("Would you like to download file ? (y/n): ")
    if order == 'y':
        client_receiver()
    else:
        print('-- Connection closed --')
