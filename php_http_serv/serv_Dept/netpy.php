<?php
// sudo php -S 127.0.0.1:6777 netpy.php
session_start();
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="Utf-8" />
        <link rel="stylesheet" href="index.css" type="text/css" />
        <title>Proxy display</title>
    </head>
    <body>
        <h1>Network cmd data :</h1>

        <h2>ifconfig : (system)</h2>
        <?php
        echo '<pre>';
        $last_line = system('ifconfig', $retval);
        echo '</pre>
        <hr />Last line of the output: ' . $last_line . '
        <hr />Return value: ' . $retval;
        ?>
        <br><br/>

        <h2>netstat -tulpn : (system)</h2>
        <?php
        echo '<pre>';
        $last_line = system('netstat -tulpn', $retval);
        echo '</pre>
        <hr />Last line of the output: ' . $last_line . '
        <hr />Return value: ' . $retval;
        ?>
        <br><br/>

        <h2>route -n : (system)</h2>
        <?php
        echo '<pre>';
        $last_line = system('route -n', $retval);
        echo '</pre>
        <hr />Last line of the output: ' . $last_line . '
        <hr />Return value: ' . $retval;
        ?>
        <br><br/>

        <h2>cat /etc/hosts : (system)</h2>
        <?php
        echo '<pre>';
        $last_line = system('cat /etc/hosts', $retval);
        echo '</pre>
        <hr />Last line of the output : ' . $last_line . '
        <hr />Return value: ' . $retval;
        ?>
        <br><br/>

        <h2>curl icanhazip.com : (system)</h2>
        <?php
        echo '<pre>';
        $last_line = system('curl icanhazip.com', $retval);
        echo '</pre>
        <hr />Your public IP : ' . $last_line . '
        <hr />Return value: ' . $retval;
        ?>
        <br><br/>

    </body>
</html>
