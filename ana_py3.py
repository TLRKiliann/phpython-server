#!/usr/bin/python3

"""
    To get public IP
"""

from requests import get
import sys
import os

os.system("xfce4-terminal -e 'bash -c \"netstat -tpe; exec bash\"'")

url = "http://icanhazip.com"
print("CHECK public IP from : {}".format(url))

r = get(url).text
print(r)

print("your IP Address is : {}".format(r))
