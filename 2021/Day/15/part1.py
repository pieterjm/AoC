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

    # if current position is the destination
    if pos[0] == nrows - 1 and pos[1] == ncols - 1:
        if score + grid[pos[0]][pos[1]] < minscore:
            minscore = score + grid[pos[0]][pos[1]]
            minpath = path + pos
            print("new minimum",minscore)
        return
        
    # potential directions are up,down,left,right # for now we only look right or down
    directions = [[pos[0]+1,pos[1]],[pos[0],pos[1]+1]] #,[pos[0]-1,pos[1]],[pos[0],pos[1]-1]]:
    minpscore = 10
    for p in directions:
        if 0 <= p[0] < nrows and 0 <= p[1] < ncols:
            minpscore = min(grid[p[0]][p[1]],minpscore)

    #
    for p in directions:
        # only if p is in the grid and only if p has not been visited before
        if 0 <= p[0] < nrows and 0 <= p[1] < ncols:
            if not p in path:                
                if grid[p[0]][p[1]] == minpscore:
                    if (score + grid[p[0]][p[1]] + nrows - p[0] + ncols - p[1]) < minscore:
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
    # Implement dijkstra's algorithm

    # keep track of visited nodes and distance to the start node, if distance is 0, it has not been visited
    d = []
    v = []
    for r in range(nrows):
        rowd = []
        rowv = []
        for c in range(ncols):
            rowd.append(1000000000)
            rowv.append(False)
        d.append(rowd)
        v.append(rowv)
        
    # initial position
    current = [0,0]
    d[0][0] = 0
    v[0][0] = True
    path = [current]

    # create list of nodes adjacent to the path
    for s in range (ncols * nrows):
        print(s)
        r = current[0]
        c = current[1]


        # find adjacent nodes and update distance
        for p in [[r,c-1],[r,c+1],[r-1,c],[r+1,c]]:
            if 0 <= p[0] < nrows and 0 <= p[1] < ncols and v[p[0]][p[1]] == False:
                # distance to neighbour
                distance = d[r][c] + grid[p[0]][p[1]]
                if distance < d[p[0]][p[1]]:
                    d[p[0]][p[1]] = distance

        # mark as visited
        v[r][c] = True

                    
        # new current is lowest score
        mindist = 10000000
        current = [0,0]
        for r in range(nrows):
            for c in range(ncols):
                if d[r][c] < mindist:
                    if v[r][c] == False:
                        current = [r,c]
                        mindist = d[r][c]

    print(d[nrows-1][ncols -1])
                
filename = sys.argv[1]
print(doit(filename))


