<?php
// On démarre la session (ceci est indispensable dans toutes les pages de notre section membre)
session_start ();
// On récupère nos variables de session
if (isset($_SESSION['pseudo'])) 
{
    // On teste pour voir si nos variables ont bien été enregistrées
    $_SESSION['pseudo'] = htmlspecialchars(strip_tags($_SESSION['pseudo']));
}
else 
{
    echo 'La variable n\'est pas déclarée.';
}
?>

<!DOCTYPE html>

<html>
    <head>
        <title>Proxy request</title>
    </head>

    <body>
        <h3>You are on ip_address :</h3>
            <div classe="basdp">
                <div class="pgview">
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
                    //Affichage de l'IP:
                    echo '<p>Votre ip publique : ' . $ip . '</p>';
                    //Récupération de la Date et Heure
                    $date = date("d-m-Y");
                    $heure = date("H:i");
             
                    // Enregistrement dans un fichier.txt
                    $fp =fopen("ip_registrer.txt","a");
                    fputs ($fp,  " $ip || $date || $heure\n ");
                    fclose($fp);
                    ?>
                </div>
            </div>
    </body>
</html>