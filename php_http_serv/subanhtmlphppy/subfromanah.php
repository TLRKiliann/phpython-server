<?php
// Execute to an other shell => sudo php -S 127.0.0.1:80
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="Utf-8" />
        <link rel="stylesheet" href="subfromanah.css" type="text/css" />
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
            $fp =fopen("subip_registrer.txt", "a");
            fputs ($fp,  " $ip || $date || $heure ");
            fclose($fp);
            ?>
        </div>
    <p>Well done with python3 !!!</p>
    </body>
</html>
