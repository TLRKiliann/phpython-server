<?php
// sudo php -S 127.0.0.1:6888 php_httphead.php
// Run firefox &
// Enter : 127.0.0.1:6888
// View page source on your browser;)
session_start();
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="Utf-8" />
        <link rel="stylesheet" href="index.css" type="text/css" />
        <title>php display http meta data</title>
    </head>

    <body>
        <h1>Analyze HTTP meta data with php :</h1>
        <h2>stream_get_meta_data() : (system)</h2>
        <?php
        $url = 'http://example.com/';
        if(!$fp = fopen($url, 'r'))
        {
            trigger_error("Unable to open URL ($url)", E_USER_ERROR);
        }
        $meta = stream_get_meta_data($fp);
        print_r($meta);
        fclose($fp);
        ?>
        <br><br/>
        <h2>get_headers</h2>
        <?php
        $url = 'http://example.com';
        print_r(get_headers($url));
        print_r(get_headers($url, 1));
        ?>
        <br><br/>
        <?php
        function parseHeaders( $headers )
        {
            $head = array();
            foreach( $headers as $k=>$v )
            {
                $t = explode( ':', $v, 2 );
                if( isset( $t[1] ) )
                    $head[ trim($t[0]) ] = trim( $t[1] );
                else
                {
                    $head[] = $v;
                    if( preg_match( "#HTTP/[0-9\.]+\s+([0-9]+)#",$v, $out ) )
                        $head['reponse_code'] = intval($out[1]);
                }
            }
            return $head;
        }
        print_r(parseHeaders($http_response_header));
        ?>
        <h2>http_response_header</h2>
        <?php
        function get_contents() {
          file_get_contents("http://example.com");
          var_dump($http_response_header);
        }
        get_contents();
        var_dump($http_response_header);
        ?>

        <h3>!!! See view page source for a pretty much more presentation !!!</h3>
    </body>
</html>