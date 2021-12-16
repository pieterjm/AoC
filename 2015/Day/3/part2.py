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

    house = [[0,0],[0,0]]
    visited = {}
    visited["{}:{}".format(0,0)] = 2
    s = 0
    
    file = open(filename, 'r')
    while True:                
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break
        line = list(line.strip())

        
        for c in line:
            s = 1 - s
            
            for d in range(2):
                house[s][d] += dir[c][d]
                id = "{}:{}".format(house[s][0],house[s][1])
                if id in visited:
                    visited[id] += 1
                else:
                    visited[id] = 1
                    
                    
    return (len(visited))    
    
filename = sys.argv[1]
print(doit(filename))


