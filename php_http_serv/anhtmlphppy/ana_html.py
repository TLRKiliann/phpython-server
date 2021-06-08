#!/usr/bin/python3

__Explain__="""
-------------------------------------------------------
########################################################

    This script allows to write in the file fromanah.php 
    and to launch the php server while opening the browser 
    with address (localhost)
    
    To run programm, execute :
    > python3 ana_html.py 

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
        <link rel="shortcut icon" href="my_icon.png" type="image/png">
        <link rel="icon" href="my_icon.png" type="image/png">
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

# To define variable for callProcFunc()
servphp = "sudo php -S 127.0.0.1:80/fromanah.php"

# Call function from procfile.py and pass var to the function
# for launching php server
procfile.callProcFunc(servphp, url)
