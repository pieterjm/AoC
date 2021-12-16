import re
import sys
import numpy as np

def doit(filename): 
    dir = {
        '^': [0,1],
        'v': [0,-1],
        '>': [1,0],
        '<': [-1,0]
        }

    house = [0,0]
    visited = {}
    visited["{}:{}".format(house[0],house[1])] = 1
    
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break
        line = list(line.strip())

        for c in line:
            for d in range(2):
                house[d] += dir[c][d]
                id = "{}:{}".format(house[0],house[1])
                if id in visited:
                    visited[id] += 1
                else:
                    visited[id] = 1
                    
                    
    return (len(visited))    
    
filename = sys.argv[1]
print(doit(filename))


