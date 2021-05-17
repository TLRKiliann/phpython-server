#!/usr/bin/python3

import socket
from threading import Thread

TCP_IP = "localhost"
TCP_PORT = 5000

class ClientThread(Thread):

    def __init__(self, ip, port, socket_server):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket_server = socket_server
        print(" New thread started for "+ip+":"+str(port))

    def run(self):
        filename = 'fileX.txt'
        f = open(filename, 'rb')
        while True:
            l = f.read(1024)
            while (l):
                self.socket_server.send(l)
                #print('Sent ',repr(l))
                l = f.read(1024)
            if not l:
                f.close()
                self.socket_server.close()
                break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print("Waiting for incoming connections...")
    (conn, (ip, port)) = tcpsock.accept()
    print('Got connection from ', (ip, port))
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
