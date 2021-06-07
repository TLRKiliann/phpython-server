#!/usr/bin/python3


__RdProc__ = """
¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢

        To launch PHP SERVER !

¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢
"""


import subprocess


def callProcFunc(phpserv):
    """
        phpserv is defined in ana_html.py script :
        phpserv = "sudo php -S 127.0.0.1:80/fromanah.php"
    """
    print(__RdProc__)
    proc = subprocess.run(phpserv, shell=True)
