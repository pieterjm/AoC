import re
from array import *
import sys

file = open(sys.argv[1], 'r')

lines = []

while True:
        line = file.readline()
        if not line:
                break
#        print(line)
        coords = line.split()
        start = coords[0].split(',')
        stop  = coords[2].split(',')
        start[0] = int(start[0])
        start[1] = int(start[1])
        stop[0] =  int(stop[0])
        stop[1] = int(stop[1])

        lines.append([start,stop])

# find max and create grid
maxx = 0
for coord in lines:
        if coord[0][0] > maxx:
                maxx = coord[0][0]
        if coord[1][0] > maxx:
                maxx = coord[1][0]                
        if coord[0][1] > maxx:
                maxx = coord[0][1]
        if coord[1][1] > maxx:
                maxx = coord[1][1]
maxx = maxx + 1
#if maxx > maxy:
#        maxy = maxx
#else:
#        maxx = maxy
#grid = [ [0]*maxx for i in range(maxx)]
grid = [[0 for x in range(maxx)] for y in range(maxx)]

for line in lines:
        start = line[0]
        stop  = line[1]


        rc = [stop[0] - start[0],stop[1] - start[1]]

        step = [0,0]
        # only hor or vert lines
        if ( rc[0] != 0 ):
                step[0] = int(rc[0] /  abs(rc[0]))
        if ( rc[1] != 0 ):
                step[1] = int(rc[1] /  abs(rc[1]))

        pos = start
        grid[pos[0]][pos[1]] = grid[pos[0]][pos[1]] + 1
                
        cont = True
        while cont:
                for i in range(2):
                        pos[i] = pos[i] + step[i]
                grid[pos[0]][pos[1]] = grid[pos[0]][pos[1]] + 1
                if (((pos[0] == stop[0]) and (pos[1] == stop[1]))):
                        cont = False

count = 0
for x in range(maxx):
        for y in range(maxx):
                if grid[x][y] > 1:
                        count = count + 1
print(count)
