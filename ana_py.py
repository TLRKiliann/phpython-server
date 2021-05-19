#!/usr/bin/python3


"""
    To log TCP connection with file "network.log"
"""


import socket
import time
import datetime
import os
import sys

 
LOG_FNAME = "network.log"
FILE = os.path.join(os.getcwd(), LOG_FNAME)

def send_ping_request(host="192.168.18.1", port=80, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        print("host: {} port {}".format(host, port))
    except OSError as error:
        print("Nothing happend")
        return False
    else:
        s.close()
        print("Connection closed")
        return True

def write_permission_check():
    try:
        with open(FILE, "a+") as file:
            pass
    except OSError as error:
        print("Log file creation failed")
        sys.exit(1)
    finally:
        pass

def calculate_time(start, stop):
    time_difference = stop - start
    seconds = float(str(time_difference.total_seconds()))
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]

def mon_net_connection(ping_freq = 2):
    monitor_start_time = datetime.datetime.now()
    motd = "Network connection monitoring started at: " +\
    str(monitor_start_time).split(".")[0] + " Sending ping request in " +\
    str(ping_freq) + " seconds"
    print(motd)
    with open(FILE, "a+") as file:
        file.write("\n")
        file.write(motd + "\n")
    while 1:
        if send_ping_request():
            time.sleep(ping_freq)
        else:
            down_time = datetime.datetime.now()
            fail_msg = "Network Connection Unavailable at: " + str(down_time).split(".")[0]
            print(fail_msg)
            with open(FILE, "a+") as file:
                file.write(fail_msg + "\n")
                i = 0
            while not send_ping_request():
                time.sleep(1)
                i += 1
                if i >= 3600:
                    i = 0
                    now = datetime.datetime.now()
                    continous_message = "Network Unavailabilty Persistent at: " + str(now).split(".")[0]
                    print(continous_message)
                    with open(FILE, "a") as file:
                        file.write(continous_message + "\n")
            up_time = datetime.datetime.now()
            uptime_message = "Network Connectivity Restored at: " + str(up_time).split(".")[0]
 
            down_time = calculate_time(down_time, up_time)
            _m = "Network Connection was Unavailable for " + down_time
 
            print(uptime_message)
            print(_m)
 
            with open(FILE, "a+") as file:
                file.write(uptime_message + "\n")
                file.write(_m + "\n")
mon_net_connection()
