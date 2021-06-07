#!/usr/bin/python3


__PROC__ = """
¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢

        To launch PHP SERVER !

¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢
"""


import subprocess


print(__PROC__)

def callProcFunc(phpserv):
    """
        phpserv is defined in ana_html.py script :
        phpserv = "sudo php -S 127.0.0.1:80/fromanah.php"
    """
    proc = subprocess.run(phpserv, shell=True)
