#!/usr/bin/python3

__OpenBrowser__="""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    This script launch webbrowser !

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

import os
import sys
import webbrowser
import subprocess

__StopServer__="""
.........................................................................
¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢
*************************************************************************

    -----------------------------------------------------------------
    |* Verify if "php server" is running, with this command line : *|
    -----------------------------------------------------------------

> ps aux | grep -i "firefox"
> ps aux | grep -i "php"
> ps aux | grep -i "python"

                  -----------------------------------
                  |* Stop "php server" as follow : *|
                  -----------------------------------

> kill $(ps aux | grep '[p]ython csp_build.py' | awk '{print $2}')
- It will stop all pid ;)

                       ------------------------
                       |* Use next command : *|
                       ------------------------
> lsof -i 
- To verify if every pid stopped !

- If you see :
...14788  1036 pts/2    S+   17:36   0:00 grep --color=auto -i php
...14788  1100 pts/1    S+   17:36   0:00 grep --color=auto -i firefox

S = interruptible sleep (waiting for an event to complete)
+ = in the foreground process group

--color=auto -i php = 

-i = --ignore-case

php = service of systemd, system V or upstart...

'https://unix.stackexchange.com/questions/236960/what-does-the-color-
auto-option-for-gnu-grep-mean'
Since grep is a GNU program another option might be having a look at 
the source code.

Internally grep tests the static int color_option for either 0,1 or 2.

    0 never use colorized output
    1 always use colors
    2 only use colors when printing to a terminal

Now when you hand over --color=auto to grep as an argument on your CLI, 
it internally sets the variable color_option to 2.

If color_option equals 2 grep then further tests whether STDOUT is linked 
to a terminal or the user disabled colorized outpit via shell environment 
variables. If the former one is true and colorized output is permitted, 
grep then continues with evaluating which colors should be used and in the 
end finally prints out to your CLI in color.

source: (grep 2.21)

grep.c line 306, 2374, 2440
colorize-posix.c line 36
> man isatty 

Click on "quit" to your browser to finish clearly process.
"Ctrl + c" to stop PHP server.

*************************************************************************
¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢
.........................................................................
"""

def callMyBrow(url):
    """
        To open browser with addr
    """
    print(__OpenBrowser__)
    os.system("xfce4-terminal -e 'bash -c \"firefox {}; exec bash\"'".format(url))
    # Open a new tab in webbrowser with url defined before :
    # webbrowser.get().open_new(url)
    print(__StopServer__)
