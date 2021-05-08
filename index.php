<?php
session_start();
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="Utf-8" />
        <link rel="stylesheet" href="index.css" type="text/css" />
        <title>Proxy request</title>
    </head>

    <body>
        <h1>SimpleHTTPServer and php server :</h1>
        <h2>- 2 server with 2 differents ports -</h2>
        <h3>server 1 : sudo php -S 127.0.0.1:80</h3>
        <h3>server 2 : python3 server.py 8000</h3>
        <h4>Results from server 1 :</h4>
            <div class="content">
                <?php
                // Récupération d'adresse IP
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
                fputs ($fp,  " $ip || $date || $heure\n ");
                fclose($fp);
                ?>
            </div>
            <tr>
                <form method="POST" action="index.php" enctype="multipart/form-data">
                    <div class="upload-wrapper">
                        <span class="file-name">Choose a file</span>
                        <label for="file-upload">from server 1 : <input type="file" id="file-upload" name="uploadedFile"></label>
                    </div>
                    <!--a href=":8000">Dowload File</a-->
                </form>
                <br><br/>
                <form method="POST" target="_blank">
                    <a>To download from server 2 : </a>
                    <button type="submit" value="1" name="pressed">Download</button>
                </form>
                <?php
                //try
                //{
                if($_POST['pressed'] == 1 )
                {
                    echo "New redirection error http 302";
                    header('Location: http://127.0.0.1:8000/');
                    #$output = shell_exec('pwd');
                    #echo "<pre>$output</pre>";
                }
                //}
                //catch (Exception $e)
                //{
                  //  echo "Some trouble !!!";
                //}
                ?>
                <!--  -->
                <h4>ls -l :</h4>
                <?php
                $command = "ls -l";
                echo "<pre>";
                echo shell_exec($command);
                echo "</pre>";
                ?>
                <h4>ls -larth :</h4>
                <?php
                echo shell_exec('ls -larth');
                ?>
                <br><br/>
                <h4>ls -larth :</h4>
                <!-- shell_exec -->
                <?php
                $cmd = "ls -larth";
                echo "<pre>" . shell_exec($cmd) . "</pre>";
                ?>
                <h4>ls -larth :</h4>
                <?php
                echo shell_exec('ifconfig -a');
                ?>
                <br><br/>
                <h4>ping -c 3 localhost</h4>
                <?php
                echo shell_exec("ping -c 3 localhost");
                ?>
                <br><br/>
                <h4>cat /var/log/syslog | grep -i 'error' :</h4>
                <?php
                echo shell_exec("cat /var/log/syslog | grep -i 'error'");
                ?>
                <br><br/>
                <h4>route -n :</h4>
                <?php
                echo shell_exec("route -n");
                ?>
                <!-- Command -->
                <br><br/>
                <h4>getcwd() :</h4>
                <?php
                echo getcwd();
                echo "<br>Youpi !!!<br/>";
                ?>
                <!-- Actual link adress -->
                <?php
                $actual_link = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
                echo "<br><h4>Actual link : </h4><pre> $actual_link </pre><br/>";
                ?>
                <?php
                $actual_link = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
                echo "<br><h4>Actual link : </h4><pre> $actual_link </pre><br/>";
                ?>
            </tr>
        <br><br/>
        <a>You can also reach server 2 by entering : "localhost:8000" in url address !</a>
    </body>
</html>