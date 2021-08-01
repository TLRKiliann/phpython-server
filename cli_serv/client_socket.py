#!/usr/bin/python3

import socket
import sys

"""
    class socketserver.TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)
    This uses the Internet TCP protocol, which provides for continuous streams of data between 
    the client and server. If bind_and_activate is true, the constructor automatically attempts 
    to invoke server_bind() and server_activate(). The other parameters are passed to the 
    BaseServer base class.
    Run at first server_socket.py
    Run prog with this cmd : python3 client_socket.py "something to write"
"""

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    # Send msg to server with bytes() or encode()
    # display result with : b'' on server
    # sock.sendall(bytes(data + "\n", "utf-8"))
    sock.sendall(data.encode())
    # Receive data from the server and shut down
    #received = str(sock.recv(1024), "utf-8")
    # or
    received = sock.recv(1024).decode()

print("\n\nSent from Client:     {}".format(data))
print("Received from Server: {}".format(received))
