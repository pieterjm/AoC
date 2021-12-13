import re
import sys
import numpy as np

def doit(filename):
    file = open(filename, 'r')

    
    line = file.readline()

     
    while True:
        count += 1
        linelen = len(line)
        for c in list('abcdefghijklmnopqrstuvwxyz'):            
            p1 = c + c.upper()
            p2 = c.upper() + c
            line = line.replace(p1,"")
            line = line.replace(p2,"")
            
        if len(line) == linelen:
            return len(line)
                    
filename = sys.argv[1]
print(doit(filename))


