import re
import sys
import numpy as np

def doit(filename):
    file = open(filename, 'r')

    claims = []
    
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break
        line = line.rstrip().lstrip()
        
        # #1 @ 342,645: 25x20
        m = re.search('^\#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$',line)
        if m:
            claims.append({
                'id': int(m.group(1)),
                'x': int(m.group(2)),
                'y': int(m.group(3)),
                'w': int(m.group(4)),
                'h': int(m.group(5))})
        else:
            print("problem in line: {}".format(line))
            sys.exit(0)

    maxx = 0
    maxy = 0
    for claim in claims:
        if claim['x']+claim['w'] > maxx:
            maxx = claim['x']+claim['w']
        if claim['y']+claim['h'] > maxy:
            maxy = claim['y']+claim['h']

    grid = []
    for x in range(maxx):
        row = []
        for y in range(maxy):
            row.append(0)
        grid.append(row)


    for claim in claims:
        for x in range(claim['x'],claim['x']+claim['w']):
            for y in range(claim['y'],claim['y']+claim['h']):
                grid[x][y] += 1

    sum = 0
    for x in range(maxx):
        for y in range(maxy):
            if grid[x][y] > 1:
                sum += 1
    

    return sum
            
    
filename = sys.argv[1]
print(doit(filename))


