<?php
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
