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
    #url = "https://www.google.com"
    print(__OpenBrowser__)
    os.system("xfce4-terminal -e 'bash -c \"sudo python3 ana_pkt.py; exec bash\"'")
    #subprocess.run(["xfce4-terminal", "-x", "sudo python3 ana_pkt.py"])
    webbrowser.get().open_new(url)
