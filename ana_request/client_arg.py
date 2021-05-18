#!/usr/bin/python3

import socket
import sys

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Enter an address with a port number to validate CMD line !")
    sys.exit(1)

print("get addr : {}".format(ip))
print("get port : {}".format(port))


# Create socket for server
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Ctrl+c to exit the program !")
socket_client.connect((ip, int(port)))

# Let's send data through TCP protocol
while 1:
    send_data = input("Type some text to send => ");
    socket_client.sendto(send_data.encode('utf-8'), (ip, int(port)))
    print("\n\n 1. Client sent : ", send_data, "\n\n")
    ask_cli = input("Would you like to wait for answer ? (y/n) : ")
    if ask_cli == "n":
        break
    else:
        pass
    print("Waiting on server...")
    print("Ctrl+c to exit the program !")
    data, address = socket_client.recvfrom(1024)
    print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")
# close the socket
socket_client.close()
