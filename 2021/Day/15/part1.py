import re
import sys
import numpy as np

grid = []
nrows = ncols = 0
minscore = 0
minpath = []

def walk(path,score):
    global grid,nrows,ncols,minscore,minpath

    # get the current position
    pos = path[-1]
        
    # potential directions are up,down,left,right
    for p in [[pos[0]+1,pos[1]],[pos[0],pos[1]+1]]: #,[pos[0]-1,pos[1]],[pos[0],pos[1]-1]]:
        # only if p is in the grid and only if p has not been visited before
        if 0 <= p[0] < nrows and 0 <= p[1] < ncols and p not in path and (score + grid[p[0]][p[1]] + nrows - p[0] + ncols - p[1]) < minscore:
            # if we reached the end, check if this path is better, and also stop further examination
            if p[0] == nrows - 1 and p[1] == ncols - 1:
                if score + grid[p[0]][p[1]] < minscore:
                    minscore = score + grid[p[0]][p[1]]
                    minpath = path + p
                    print(minscore)

                # always return
                return
            else:
                walk(path + [p],score + grid[p[0]][p[1]])
            
            
            


def doit(filename):
    global grid,nrows,ncols,minscore,minpath
    
    file = open(filename, 'r')

    # read the grid
    grid = []
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:            
            break

        items = list(line.strip())
        for i in range(len(items)):
            items[i] = int(items[i])
        grid.append(items)

    nrows = len(grid)
    ncols = len(grid[0])
    print("rows = {}, cols = {}".format(nrows,ncols))

    # First approach
    # Calculate the start minimal score and path of an arbitrary line (diagonal snake)
    # Then walk through the grid towards the destination, if score larger than minimal, stop walking
    # The instructions are not clear on wether we are allowed to walk back, so assuming that this is allowed
    # construct a path (array of points on the grid), walk to next points (not already on the path) stop path if above minimum
    # if a path is found adjust minimum
    # this solution works for a 10x10 grid, but is way too costly for a 100x100 grid
    #
    # second approach
    # start at the top left and select the lowest neighbour to the right or bottom, if multiple neighbours are present, only walk
    # in those directions

    
    # first step on the path is topleft corner
    path = [[0,0]]
    minpath = []
    
    minscore = 0
    print(grid)    
    for r in range(nrows - 1):        
        minscore += grid[r][r] + grid[r+1][r]
    print(minscore)
    walk(path,0)
    
    
    
    
    
filename = sys.argv[1]
print(doit(filename))


