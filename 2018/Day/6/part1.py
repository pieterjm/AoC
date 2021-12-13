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
    

    grid = []
    for r in range(maxl[0]):
        row = []
        for c in range(maxl[1]):
            minmd = maxl[0] + maxl[1]
            minloc = -1
            for l in range(len(locs)):
                loc = locs[l]
                md = abs(loc[0]-r) + abs(loc[1]-c)
                if md < minmd:
                    minmd = md
                    minloc = l
                elif md == minmd:
                    minloc = -1
            row.append(minloc)
        grid.append(row)


    area = {}

    for r in range(maxl[0]):
        for c in range(maxl[1]):
            if (((r == 0) or (r == (maxl[0] - 1)))or((c == 0 or c == (maxl[1] - 1)))):
                border = True
            else:
                border = False
            
            if grid[r][c] in area:
                area[grid[r][c]][0] += 1
                if border:
                    area[grid[r][c]][1] = border
            else:
                area[grid[r][c]] = [1,border]

    maxsize = 0
    for key in area:
        if area[key][1] == False:
            if area[key][0] > maxsize:
                maxsize = area[key][0]

    return maxsize
filename = sys.argv[1]
print(doit(filename))


