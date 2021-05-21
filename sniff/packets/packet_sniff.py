#!/usr/bin/python3

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For http://bitforestinfo.blogspot.com
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
################### Thanks #######################
##################################################
#
#
__author__='''
######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''

import socket
import struct
import binascii
import os
import pye

print(pye.__author__)

as_ip = input("Enter IP to sniff : ")

if os.name == "nt":
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    # bind is for listening sockets...
    s.bind((as_ip, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
else:
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
    # socket.PF_PACKET
    # socket.SOCK_RAW
    # socket.ntohs()

while True:
    print("<<<<<<<<<<<<< HEAD")
    pkt = s.recvfrom(65565)
    unpack = pye.unpack()
    print("\n\n===>> [+] --- Ethernet Header --- [+]")
    for i in unpack.eth_header(pkt[0][0:14]).items():
        a, b = i
        print("{} : {} | ".format(a,b),)
    print("\n===>> [+] ------ IP Header ------ [+]")
    for i in unpack.ip_header(pkt[0][14:34]).items():
        a, b = i
        print("{} : {} | ".format(a,b),)
    print("\n===>> [+] -+-+-+-+-+-+- Tcp Header -+-+-+-+-+-+- [+]")
    for  i in unpack.tcp_header(pkt[0][34:54]).items():
        a, b = i
        print("{} : {} | ".format(a, b),)

    print("=======")
    pkt=s.recvfrom(65565)
    unpack=pye.unpack()
    print("\n\n===>> [+] ------------ Ethernet Header----- [+]")
    for i in unpack.eth_header(pkt[0][0:14]).items():
        a,b=i
        print("{} : {} | ".format(a,b),)
    print("\n===>> [+] ------------ IP Header ------------[+]")
    for i in unpack.ip_header(pkt[0][14:34]).items():
        a,b=i
        print("{} : {} | ".format(a,b),)
    print("\n===>> [+] ------------ Tcp Header ----------- [+]")
    for  i in unpack.tcp_header(pkt[0][34:54]).items():
        a,b=i
        print("{} : {} | ".format(a,b),)

    print(">>>>>>>>>>>>>> master")
