import re
import sys
import numpy as np

def doit(filename):
    file = open(filename, 'r')


    maxl = [0,0]
    locs = []
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break

        loc = line.split(',')
        loc = list(map(int,loc))
        locs.append(loc)
        for i in range(2):
            if loc[i] > maxl[i]:
                maxl[i] = loc[i]
        for i in range(2):
            maxl[i] += 1
    

    size = 0
    for r in range(maxl[0]):
        for c in range(maxl[1]):
            summd = 0
            for l in range(len(locs)):
                loc = locs[l]
                summd +=  abs(loc[0]-r) + abs(loc[1]-c)
                
            if summd < 10000:
                size += 1
    return size


filename = sys.argv[1]
print(doit(filename))


