#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Launch prog with : python3 nmap_target.py
    Enter address : 127.0.0.1 or public_IP
    You can use : ps f | grep -i "python"
    for seeing if python process run
    or your internet interface :
    sudo iftop -i <eth0, enp3s0 or other (ifconfig)>
"""

import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer = input("Enter a remote host to scan : ")
# You could choose socket.getfqdn().gethostbyaddr() but don't
# let getfqdn empty, otherwise it will return for localhost.
askmyip = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", askmyip)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)
# We also put in some error handling for catching errors

try:
    for port in range(49, 81):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((askmyip, port))
        if result == 0:
            print("Port {}: 		Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print('Scanning completed in : {} sec.'.format(total))
