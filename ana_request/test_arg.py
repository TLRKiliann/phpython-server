#!/usr/bin/python3

import getopt
import sys
 
first =""
last =""
argv = sys.argv[1:]
try:
    options, args = getopt.getopt(argv, "f:l:",
                               ["first =",
                                "last ="])
except:
    print("Error Message ")
 
for name, value in options:
    if name in ['-f', '--first']:
        first = value
    elif name in ['-l', '--last']:
        last = value
 
print(first + " " + last)

import sys
if __name__ == '__main__':
    for idx, arg in enumerate(sys.argv):
       print("Argument #{} is {}".format(idx, arg))
    print ("Number of arguments passed is : ", len(sys.argv))
