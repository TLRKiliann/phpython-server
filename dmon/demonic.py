#!/usr/bin/python3

import sys
import threading
import time

class TestThread(threading.Thread):
    def __init__(self, daemon):
        threading.Thread.__init__(self)
        self.daemon = daemon

    def run(self):
        x = 0
        while 1:
            if self.daemon:
                print("Daemon :: %s" % x)
            else:
                print("Non-Daemon :: %s" % x)
            x += 1
            time.sleep(1)

if __name__ == "__main__":
    print("__main__ start")
    if sys.argv[1] == "demonic":
        thread = TestThread(True)
    else:
        thread = TestThread(False)
        sys.exit(1)
    thread.start()
    time.sleep(5)
    print("__main__ stop")
