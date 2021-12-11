import re
import sys
import numpy as np

def printgrid(grid):
    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[r])):
            line += "" + str(grid[r][c])
        print(line)
            
def step(grid):
    # increase energy of each octopus
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1

def flash(grid):
    # check and fire flashes
    cont = True
    numflash = 0
    while cont:
        cont = False
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] > 9:
                    numflash += 1
                    cont = True
                    grid[r][c] = 0
                    for [i,j] in [[r-1,c-1],[r-1,c],[r-1,c+1],[r,c-1],[r,c+1],[r+1,c-1],[r+1,c],[r+1,c+1]]:
                        if 0 <= i < len(grid) and 0 <= j < len(grid[r]):
                            if grid[i][j] > 0:
                                grid[i][j] += 1
    return numflash
                            
def doit(filename):
        file = open(filename, 'r')
        points = []

        grid = []
        while True:
                line = file.readline()
                if not line:
                        break
                if len(line) == 0:
                        break
                line = line.rstrip().lstrip()
                line = list(line)
                for i in range(len(line)):
                    line[i] = int(line[i])
                grid.append(list(line))

        numflash = 0

        for s in range(100):
            step(grid)
            numflash += flash(grid)

        return numflash
    
filename = sys.argv[1]
print(doit(filename))


