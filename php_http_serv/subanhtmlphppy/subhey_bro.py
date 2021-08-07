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
ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢¢ŋ¢ŋ¢ŋ¢
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

S = interruptible sleep (waiting for an event to complete)
+ = in the foreground process group

--color=auto -i php = 

'https://unix.stackexchange.com/questions/236960/what-does-the-color-
auto-option-for-gnu-grep-mean'
Since grep is a GNU program another option might be having a look at 
the source code.

Internally grep tests the static int color_option for either 0, 1 or 2.

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

> grep.c line 306, 2374, 2440
> colorize-posix.c line 36
> man isatty 

*************************************************************************
ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢ŋ¢¢ŋ¢ŋ¢ŋ¢
.........................................................................
"""

def callMyBrow(url):
    print(__OpenBrowser__)
    os.system("xfce4-terminal -e 'bash -c \"firefox 127.0.0.1:80/subfromanah.php &; exec bash\"'")
    webbrowser.get().open_new(url)
    print(__StopServer__)
