#!/usr/bin/python3

import socketserver

"""
    1) Run prog with this cmd : python3 server_socket.py
    2) Run client_socket like this : python3 client_socket "write something"
"""

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
        The request handler class for our server.
        It is instantiated once per connection to the server, and must
        override the handle() method to implement communication to the
        client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("[+] {} wrote:".format(self.client_address[0]))
        print(format(self.data))
        # Send back to client same 
        # data with upper-cased
        self.request.sendall(self.data.upper())
        self.request.sendall("\n[+] ACK from TCP Server".encode())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    print("[+] Server waiting new connection...")
    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
