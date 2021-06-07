<?php
// execute to an other shell => php -S 127.0.0.1:8000 dispy_data.php
// This script show you how to display data from php commands and
// from python3 commands.
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
        <h1>Differents ways to show you how to display output :</h1>

        <h2>ls -larth : (system)</h2>
        <?php
        echo '<pre>';
        $last_line = system('ls -larth', $retval);
        echo '</pre>
        <hr />Last line of the output: ' . $last_line . '
        <hr />Return value: ' . $retval;
        ?>
        <br><br/>

        <h2>ls -larth : (shell_exec)</h2>
        <?php
        echo shell_exec('ls -larth');
        ?>
        <br><br/>

        <h2>ls -larth : (exec)</h2>
        <?php
        exec('ls -larth', $outdata);
        print_r($outdata);
        ?>
        <br></br>

        <h2>netstat -tulpn : (system)</h2>
        <?php
        echo '<pre>';
        $last_line = system('netstat -tulpn', $retval);
        echo '
        </pre>
        <hr />Last line of the output: ' . $last_line . '
        <hr />Return value: ' . $retval;
        ?>
        <br><br/>

        <h2>netstat -tulpn : (exec)</h2>
        <?php
        $output=null;
        $retval=null;
        exec('netstat -tulpn', $output, $retval);
        echo "Returned with status $retval and output:\n";
        print_r($output);
        ?>
        <br><br/>

        <h2>uname -a : (exec + shell_exec)</h2>
        <?php
        //Execude command in the shell with PHP exec() function
        //put the output to the $output variable 
        exec("uname -a",$output,$return_val);
        echo "<p><p/>";
        print_r($output);
        echo "<p></p>";
        //Execute command in the shell with PHP shell_exec() function
        //put the output into $out variable
        $out = shell_exec("uname -a");
        echo $out;
        ?>
    </body>
</html>
