#!/usr/bin/python3

"""
    To get public IP
"""

from requests import get

url = "http://icanhazip.com"
print("CHECK public IP from : {}".format(url))

r = get(url).text
print(r)

print("your IP Address is : {}".format(r))
