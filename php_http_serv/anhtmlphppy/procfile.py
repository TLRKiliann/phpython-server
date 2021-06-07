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
    proc = subprocess.Popen(phpserv, stderr=subprocess.PIPE, shell=True)
    # To display error in shell, and to exit php server cleanly
    # Change value of port in ana_html.py by 443 (required root mode)
    # Test it ! When you quit webbrowser, php server run with pid
    # use this cmd for killing process : 
    # ps aux | grep "php"
    print("=> Stderr output : %s" % repr(proc.stderr))
    if proc.stderr == b'' :
        # If error occured, this line print stderr in shell
        print("=> Stderr output : %s" % repr(proc.stderr))
    else:
        pass
