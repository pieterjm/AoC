import re
import sys
import numpy as np

def doit(filename): 
    file = open(filename, 'r')

    line = file.readline()
    line = line.rstrip().lstrip()


    dir = {'(':1,')':-1}

    pos = 0
    floor = 0
    for c in list(line):
        pos += 1
        floor += dir[c]
        if floor == -1:
            return pos
    
    
filename = sys.argv[1]
print(doit(filename))


