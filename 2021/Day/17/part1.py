import re
import sys
import numpy as np


def doit(filename):
    targetx = targety = []
    
    file = open(filename, 'r')
    line = file.readline().strip()
    m = re.search("^target area: x=([0-9\-]+)\.\.([0-9\-]+), y=([0-9\-]+)\.\.([0-9\-]+)$",line)
    if m:
        targetx = [int(m.group(1)),int(m.group(2))]
        targety = [int(m.group(3)),int(m.group(4))]
    else:
        print("no match")
        sys.exit(0)
        
    vy = targety[0]
    height = targety[0]
    while vy < 0:
        height -= vy
        vy += 1
    return height
                
filename = sys.argv[1]
print(doit(filename))


