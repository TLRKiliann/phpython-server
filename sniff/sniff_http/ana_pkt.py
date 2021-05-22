#!/usr/bin/python3

__Analyzer__="""
    Recover packets to extract
    src IP and dest IP. Required
    to build 3 files to call
    terminal window...
"""

import os
import socket
import struct

print(__Analyzer__)

#sub = os.system("xfce4-terminal -e 'bash -c \"firefox; exec bash\"'")
#sub = webbrowser.open(url)
# sub = webbrowser.get().open_new(url)
#subprocess.run(["xfce4-terminal", "-x", "python3 hey_bro.py"])
#webbrowser.get().open_new(url)

# Enter ip of your internet interface :
as_ip = input("\nEnter IP of ethernet interface to sniff : ")

# To get addr source and destination
class unpack():
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
    #For Windows
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    # bind is for listening sockets...
    s.bind((as_ip, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
else:
    # For Linux
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

while True:
    print("<<<<<<<<<<<<< HEAD")
    pkt = s.recvfrom(65565)
    dpack = unpack()
    print("\n===>> [+] ------ IP Header ------ [+]")
    for i in dpack.ip_header(pkt[0][14:34]).items():
        a, b = i
        print("{} : {} | ".format(a,b),)
