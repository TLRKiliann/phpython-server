#!/usr/bin/python3

__OpenBrowser__="""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    This script launch webbrowser !

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

import os
import sys
import webbrowser
import subprocess


def callMyBrow(url):
    print(__OpenBrowser__)
    os.system("xfce4-terminal -e 'bash -c \"firefox 127.0.0.1:80/\
        fromanah.php &; exec bash\"'")
    webbrowser.get().open_new(url)
