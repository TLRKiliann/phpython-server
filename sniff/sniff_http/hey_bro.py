#!/usr/bin/python3

__OpenBrowser__="""
    One manner to get http packet
    with this method.
"""

#import subprocess
import os
import sys
import webbrowser

def callMyBrow(url):
    # url = prefix + ask 
    print(__OpenBrowser__)
    os.system("xfce4-terminal -e 'bash -c \"sudo python3 ana_pkt.py; exec bash\"'")
    webbrowser.get().open_new(url)
