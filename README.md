# proxyserv
Server demo to identificate some elements of http headers
and some files whose working as server with a proxy.

# Many libraries and modules :
- SimpleHTTPRequestHandler 
- socketserver
- TCPServer
- http.server

# Some tricks to understand how it work :
- To launch server with a listner port :
> python -m http.server 8000
Enter localhost:8000 into browser

- To download file start cmd :
> php -S  127.0.0.1:80 (-t .)
Enter 127.0.0.1:80 into browser

Case 1 :
Launch : sudo php -S 127.0.0.1:8080
This file call index.php and index.css
You can read it with your browser.
Now, launch : python3 server2.py and see
that index could be read by server2.

Case 2 :
Launch : sudo php -S 127.0.0.1:8080
and launch : python3 server2.py.

Under work and devlopement...
