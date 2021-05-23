#!/usr/bin/python3

__OpenBrowser__="""
+++++++++++++++++++++++++++++++++++++++
    - Second script called to start 
      browser with url and launch 
      ana_pkt.py in a new terminal.
+++++++++++++++++++++++++++++++++++++++
"""

import os
import sys
import webbrowser

def callMyBrow(url):
    """
        Start browser with url
        and launch ana_pkt.py in
        a new terminal.
    """
    print(__OpenBrowser__)
    os.system("xfce4-terminal -e 'bash -c \"sudo python3 ana_pkt.py; exec bash\"'")
    webbrowser.get().open_new(url)
