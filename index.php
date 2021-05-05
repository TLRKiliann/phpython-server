<!DOCTYPE html>
<html>
    <head>
        <meta charset="Utf-8" />
        <link rel="stylesheet" href="index.css" type="text/css" />
        <title>Proxy request</title>
    </head>

    <body>
        <h3>ip_address_id:</h3>
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
                            <span class="file-name">Choose a file...</span>
                            <label for="file-upload">Browse<input type="file" id="file-upload" name="uploadedFile"></label>
                        </div>
                        <!--a href=":8000">Dowload File</a-->
                    </form>
                    <form METHOD="POST" TARGET="_BLANK">
                        <button TYPE="submit" VALUE="1" name="pressed">Click</button>
                    </form>
                    <?php
                    if($_POST['pressed'] == 1 )
                    {
                        header('Location: http://127.0.0.1:8000/');
                        shell_exec('');
                    }
                    ?>
                    <!--input type="submit" class="button", name=butt, value="Upload!"-->
                </tr>
        <h3>You can also use url addess bar to put : "localhost:8000"</h3>
    </body>
</html>