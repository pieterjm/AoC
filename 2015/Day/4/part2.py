import re
import sys
import numpy as np
import hashlib

def doit(filename): 
    file = open(filename, 'r')
    line = file.readline().strip()

    i = 1
    while True:
        message = line + str(i)
        h = hashlib.md5(message).hexdigest()
        if h[:6] == "000000":
            print(h)
            return i
        i += 1

    
filename = sys.argv[1]
print(doit(filename))


