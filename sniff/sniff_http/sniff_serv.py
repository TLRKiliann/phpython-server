#!/usr/bin/python3

__Explanations__="""
    One manner to get http packet
    with this method.
"""

__Extract__="""
    Extract traffic IP from your
    ethernet interface (ifconfig)
    and look at enps0 or eth0 to
    catch ip addr.
"""

import requests
import urllib.request
import urllib.error
import socket
import subprocess
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

subprocess.run(["ping", "-c", "1", ask])
hey_bro.callMyBrow(url)
