#!/usr/bin/python3


import socket
import threading


TCP_IP = socket.gethostbyname("127.0.0.1")
TCP_PORT = 5000


class ClientThread(threading.Thread):
    """
        By convention we use threading.Thread
        for class and to instantiate function.
    """
    def __init__(self, ip, port, socket_server):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket_server = socket_server
        print("+ New thread started for " + ip + ":" + str(port))

    def run(self):
        print("Connection from : " + ip + ":" + str(port))
        filename = 'fileX.txt'
        f = open(filename, 'rb')
        l = f.read(1024)
        while (l):
           conn.send(l)
           print('Sent ', repr(l))
           l = f.read(1024)
        f.close()
        self.socket_server.close()
        #break

# socket.AF_INET=IPv4 and socket.SOCK_STREAM=TCP
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Very important socket SOL_SOCKET :set the socket option to 
# reuse the address to 1 (on/true), we pass in the "level" 
# SOL_SOCKET and the value we want it set to.
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []
i=0

while True:
    tcpsock.listen(5)
    print("+ Waiting for incoming connections...")
    try:
        (conn, (ip, port)) = tcpsock.accept()
    except error.socket as msg:
        print("+ Socket ERROR %s!" % msg)
    except TypeError as msg_ret:
        print("+ Type ERROR %s!" % msg_ret)
    print('+ Got connection from ', (ip, port))
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)
    # Number of thread
    i += 1
    print("+ Thread : ", i)

    outgo = input("+ Continue ? (y/n): ")
    if outgo == "n":
        break
    else:
        print("-.- Continue -.-")

for t in threads:
    t.join()
    print("? is t(=thread) alive ? : {}".format(t.is_alive()))
    print("+ Printable_threads : ", threads[:])
