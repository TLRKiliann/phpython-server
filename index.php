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
                    <td></td>
                      <form method="POST" action="index.php" enctype="multipart/form-data">
                        <div class="upload-wrapper">
                          <span class="file-name">Choose a file...</span>
                          <label for="file-upload">Browse<input type="file" id="file-upload" name="uploadedFile"></label>
                        </div>
                     
                        <input type="submit" name="uploadBtn" value="Upload" />
                      </form>
                    </td>
                </tr>
        <h3>Put : "localhost:8000" (to fill url space on top of youre browser !)</h3>
    </body>
</html>