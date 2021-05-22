#!/usr/bin/python3

__Explanations__="""
    One manner to get http packet
    with this method. HTTP_version = 1.0
    but it seems to work with HTTP 2.0
"""

import requests
import urllib.request
import urllib.error
 
# Take input any valid URL
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
print("\n--- SERVER ---")
print('Response server = ', urlResponse.info()["Server"])
