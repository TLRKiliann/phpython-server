#!/usr/bin/python3

__Explain__="""
-------------------------------------------------------
########################################################

    To write html code to fromanah.php with python3
    Execute :
    python3 ana_html.py 
    and then :
    firefox fromanah.html
    (html extension for seeing what we do,
    change to fromanah.php for next cmd)
    launch php serveur with this cmd :
    sudo php -S 127.0.0.1:80/fromanah.php
    Go to webbrowser and enter :
    127.0.0.1:80/fromanah.php
    You don't need to launch webbrowser, because
    it's automata.

########################################################
-------------------------------------------------------
"""

import os
import sys
import codecs
import time
import socket
import requests
from urllib.parse import urlunparse
import subprocess
import hey_bro
import procfile 


# to open/create a new html file in the write mode
f = open( 'fromanah.php', 'w')
  
# the html code which will go in the file fromanah.php
html_template = """<?php
// Execute to an other shell => sudo php -S 127.0.0.1:80
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="Utf-8" />
        <link rel="stylesheet" href="fromanah.css" type="text/css" />
    </head>
    <body>
    <h1>Wellcome to Ana-H site !</h1>
        <div class="content">
            <?php
            // To retrieve IP address
            function get_ip()
            {
                if(isset($_SERVER['HTTP_X_FORWARDED_FOR']))
                {
                    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
                }
                elseif(isset($_SERVER['HTTP_CLIENT_IP']))
                {
                    $ip = $_SERVER['HTTP_CLIENT_IP'];
                }
                else
                { 
                    $ip = $_SERVER['REMOTE_ADDR'];
                }
                return $ip;
            }
            $ip = get_ip();
            echo '<p>Your publique ip : ' . $ip . '</p>';
            $date = date("d-m-Y");
            echo '<p>Date : ' . $date . '</p>';
            $heure = date("H:i");
            echo '<p>Hour : ' . $heure . '</p>';
            $fp =fopen("ip_registrer.txt", "a");
            fputs ($fp,  " $ip || $date || $heure ");
            fclose($fp);
            ?>
        </div>
    <p>Well done with python3 !!!</p>
    </body>
</html>
"""
  
# writing the code into the file
f.write(html_template)
  
# close the file
f.close()
  
# viewing html or php files
# below code creates a 
# codecs.StreamReaderWriter object
file = codecs.open("fromanah.php", 'r', "utf-8")

# using .read method to view the html 
# php code from our object
print(file.read())

print(__Explain__)
time.sleep(1)

port = 80
url = '{}://127.0.0.1:80/fromanah.php'.format(socket.getservbyport(port))
print(url)

# To call hey_bro.py for launching function callMyBrow(url) :
hey_bro.callMyBrow(url)

phpserv = "sudo php -S 127.0.0.1:80/fromanah.php"
procfile.callProcFunc(phpserv)

# But webbrowser will cannot start at first page (new PID launched...)
#To test subprocess with stdout and stderr :
# stdout=subprocess.PIPE, stderr=subprocess.PIPE

"""
print("Result php stderr : %s" % repr(proc.stdout))
if proc.stderr == b'':
    print("=> File launched !")
elif proc.stdout == b'':
    print("=> Ok goooooooooo!")
else:
    print("=> Some trb... !")
"""