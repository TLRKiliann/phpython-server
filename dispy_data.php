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
        <h1>Differents ways to show you how to display output :</h1>

        <h4>ls -larth : (system)</h4>
        <?php
        echo '<pre>';
        $last_line = system('ls', $retval);
        echo '
        </pre>
        <hr />Last line of the output: ' . $last_line . '
        <hr />Return value: ' . $retval;
        ?>

        <br><br/>
        <h4>ls -larth : (shell_exec)</h4>
        <?php
        echo shell_exec('ls -larth');
        ?>
        <br><br/>


    </body>
</html>
