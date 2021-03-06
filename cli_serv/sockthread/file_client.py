#!/usr/bin/python3

import socket

__introcli__="""
---------------------------------------
    File Transfert with threading !
---------------------------------------
"""

print(__introcli__)

TCP_IP = socket.gethostbyname("127.0.0.1")
TCP_PORT = 5000

def client_receiver():
    # socket.AF_INET = IPv4
    # socket.SOCK_STREAM = TCP
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((TCP_IP, TCP_PORT))

    recived_f = 'fileX.txt'
    with open('file_recv.txt', 'wb') as f:
        print('[+] File opened...')
        while True:
            print('[+] Receiving data...')
            data = str(socket_client.recv(1024))
            print('[!] data=%s', repr(data))
            if not data:
                break
            # write data to a file
            added = str("YEAH !!! very good !!!")
            f.write(bytes(added, encoding="utf-8"))
            f.close()
            socket_client.close()
            print('[+] Successfully get the file')
            print('[+] Connection closed')
            print("[!] Use 'cat file_recv.txt' to see data [!]")
            break

if __name__=='__main__':
    order = input("[?] Would you like to download file ? (y/n): ")
    if order == 'y':
        client_receiver()
    else:
        print('-- Connection closed --')
