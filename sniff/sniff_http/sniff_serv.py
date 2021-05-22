#!/usr/bin/python3

__Explanations__="""
    One manner to get http packet
    with this method.
"""

__Extract__="""
    Extract traffic IP from your
    internet interface (ifconfig)
    and look at enps0 or eth0 to
    catch ip addr.
"""

import requests
import urllib.request
import urllib.error
import socket
import struct
import binascii
import os

print(__Explanations__)

# Take input any valid URL
easy = "https://"
url = input("Enter any URL address: ")
# Send request for the URL
request = urllib.request.Request(url)
r = requests.get(url)
print("\n--- header ---")
print(r.request.headers)

try:
    # Try to open the URL
    urllib.request.urlopen(request)
    print("URL Exist")
except urllib.error.HTTPError as e:
    # Print the error code and error reason
    print("Error code:%d\nError reason:%s" %(e.code, e.reason))

urlResponse = urllib.request.urlopen(url)
print("\n--- url info ---")
print(urlResponse.info())
print("\n--- SERVER ---\n")
print('Response server = ', urlResponse.info()["Server"])
print("\n\n")

print(__Extract__)

# Enter ip of your internet interface :
as_ip = input("\nEnter IP to sniff : ")

# To get addr source and destination
class unpack:
    def __cinit__(self):
        self.data = None

    # Ethernet Header
    def eth_header(self, data):
        storeobj = data

    # IP Header Extraction
    def ip_header(self, data):
        storeobj = struct.unpack("!BBHHHBBH4s4s", data)
        _source_address = socket.inet_ntoa(storeobj[8])
        _destination_address = socket.inet_ntoa(storeobj[9])
        data={"Source Address":_source_address,
        "Destination Address":_destination_address}
        return data

if os.name == "nt":
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    # bind is for listening sockets...
    s.bind((as_ip, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
else:
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

while True:
    print("<<<<<<<<<<<<< HEAD")
    pkt = s.recvfrom(65565)
    dpack = unpack()
    print("\n===>> [+] ------ IP Header ------ [+]")
    for i in dpack.ip_header(pkt[0][14:34]).items():
        a, b = i
        print("{} : {} | ".format(a,b),)
