#!/usr/bin/python3

import array
import socket
import struct

# This part of code was adapted from the Scapy project:
# https://github.com/secdev/scapy/blob/467431faf8389f745d2c16370baf6dafc5751731/scapy/utils.py#L368-L381
#
# Changes made:
# - removed use of checksum_endian_transform function
# - restructured code without modifying it
# - renamed variables
# - added type hints

"""
    sudo tcpdump -n -i eth0 -s 100 dst <ip>
    22:50:21.962026 IP ip_src.20 > ip_dst.666: Flags [FPU], 
    seq 72, win 8192, urg 0, length 0
    Flags [FPU] = FIN PUSH URGENT
"""

def chksum(packet: bytes) -> int:
    if len(packet) % 2 != 0:
        packet += b'\0'

    res = sum(array.array("H", packet))
    res = (res >> 16) + (res & 0xffff)
    res += res >> 16

    return (~res) & 0xffff


class TCPPacket:
    def __init__(self,
                 src_host:  str,
                 src_port:  int,
                 dst_host:  str,
                 dst_port:  int,
                 flags:     int = 0):
        self.src_host = src_host
        self.src_port = src_port
        self.dst_host = dst_host
        self.dst_port = dst_port
        self.flags = flags

    def build(self) -> bytes:
        packet = struct.pack(
            '!HHIIBBHHH',
            self.src_port,  # Source Port
            self.dst_port,  # Destination Port
            72,             # Sequence Number
            200,            # Acknoledgement Number
            5 << 4,         # Data Offset
            self.flags,     # Flags
            8192,           # Window
            0,              # Checksum (initial value)
            0               # Urgent pointer
        )

        pseudo_hdr = struct.pack(
            '!4s4sHH',
            socket.inet_aton(self.src_host),    # Source Address
            socket.inet_aton(self.dst_host),    # Destination Address
            socket.IPPROTO_TCP,                 # PTCL
            len(packet)                         # TCP Length
        )

        checksum = chksum(pseudo_hdr + packet)
        packet = packet[:16] + struct.pack('H', checksum) + packet[18:]
        return packet


if __name__ == '__main__':
    dst = 'ip_dst'

    pak = TCPPacket('ip_src',
        1235,
        dst,
        5575,
        0b000101001)  # Merry Christmas!

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    s.sendto(pak.build(), (dst, 0))
