#!/usr/bin/python3

__Explanations__="""
    One manner to get http packet
    and return ip src & dst.
"""

__Extract__="""
    Extract traffic IP from your
    ethernet interface (ifconfig)
    and look at enps0 or eth0 to
    catch ip addr.
"""

import urllib.error
import urllib.request
import socket
import subprocess
import requests
import hey_bro

print(__Explanations__)

# Take input any valid URL
prefix = "https://"
ask = input("Enter any URL address : https://")
url = prefix + ask
print(url)
# Send request for the URL
request = urllib.request.Request(url)
r = requests.get(url)
print("\n--- header ---")
print(r.request.headers)

try:
    # Try to open the URL
    urllib.request.urlopen(request)
    print("URL Exist")
except urllib.error.HTTPError as msg:
    # Print the error code and error reason
    print("Error code:%d\nError reason:%s" %(msg.code, msg.reason))

urlResponse = urllib.request.urlopen(url)
print("\n--- url info ---")
print(urlResponse.info())
print("\n--- SERVER ---\n")
print('Response server = ', urlResponse.info()["Server"])
print("\n\n")

__flyhost__="""
########################################################
////////////////////////////////////////////////////////

                   $$$   $$$$$$$$$$
                   $$$   $$$      $$
                         $$$      $$
                   $$$   $$$$$$$$$$
                   $$$   $$$
                   $$$   $$$
                   $$$   $$$

########################################################
////////////////////////////////////////////////////////
"""

print(__flyhost__)

IP_ADRESS = socket.gethostbyname(ask)
print("\n+ IP address of {} : {} \n".format(ask, IP_ADRESS))

__quickping__="""
########################################################
////////////////////////////////////////////////////////

        ########    ##   #####    ##   #########
        ##     ##        ##  ##   ##   ##
        ########    ##   ##   ##  ##   ##   ####
        ##          ##   ##    ## ##   ##     ##
        ##          ##   ##     ####   #########

////////////////////////////////////////////////////////
########################################################
"""

print(__quickping__)

subprocess.run(["ping", "-c", "1", ask])

# Call second file to launch browser
hey_bro.callMyBrow(url)

print(__Extract__)
