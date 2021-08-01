#!/usr/bin/python3

__Analyzer__="""
+++++++++++++++++++++++++++++++++++++
    - Recover packets to extract
      src IP and dest IP.
+++++++++++++++++++++++++++++++++++++
 """

import os
import socket
import struct

print(__Analyzer__)

# Enter ip of your internet interface :
as_ip = input("\nEnter IP of ethernet interface to sniff : ")

# To get addr source and destination
class unpack():
    def __cinit__(self):
        self.data = None

    # Ethernet Header
    def eth_header(self, data):
        storeobj = data
        storeobj = struct.unpack("!6s6sH", storeobj)
        destination_mac = binascii.hexlify(storeobj[0])
        source_mac = binascii.hexlify(storeobj[1])
        eth_protocol = storeobj[2]
        data = {"Destination Mac":destination_mac,
        "Source Mac":source_mac,
        "Protocol":eth_protocol}
        return data

    # IP Header Extraction
    def ip_header(self, data):
        storeobj = struct.unpack("!BBHHHBBH4s4s", data)
        _version = storeobj[0] 
        _tos=storeobj[1]
        _total_length = storeobj[2]
        _identification = storeobj[3]
        _fragment_Offset = storeobj[4]
        _ttl = storeobj[5]
        _protocol = storeobj[6]
        _header_checksum = storeobj[7]
        _source_address = socket.inet_ntoa(storeobj[8])
        _destination_address = socket.inet_ntoa(storeobj[9])

        data = {'Version':_version,
        "Tos":_tos,
        "Total Length":_total_length,
        "Identification":_identification,
        "Fragment":_fragment_Offset,
        "TTL":_ttl,
        "Protocol":_protocol,
        "Header CheckSum":_header_checksum,
        "Source Address":_source_address,
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
