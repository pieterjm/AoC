import re
import sys
import numpy as np

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

    # create a new grid, five times larger
    ngrid = []
    for r in range(nrows * 5):
        row = []
        for c in range(ncols * 5):
            row.append(0)
        ngrid.append(row)

    for r in range(nrows):
        for c in range(ncols):
            val = grid[r][c]
            for i in range(5):
                for j in range(5):
                    ngrid[r + i * nrows][c + j * ncols] = ((val + i + j - 1) % 9)+1
        ngrid.append(row)
    nrows = nrows * 5
    ncols = ncols * 5

    
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

    # All nodes
    edgenodes = []

    # create list of nodes adjacent to the path
    total = ncols * nrows
    stepsize = total / 100
    for s in range (total):
        if s % stepsize == 0:
            print(s /(total * 1.0))
        r = current[0]
        c = current[1]


        # find adjacent nodes and update distance
        for p in [[r,c-1],[r,c+1],[r-1,c],[r+1,c]]:
            if 0 <= p[0] < nrows and 0 <= p[1] < ncols and v[p[0]][p[1]] == False:
                edgenodes.append(p)

                # distance to neighbour
                distance = d[r][c] + ngrid[p[0]][p[1]]
                if distance < d[p[0]][p[1]]:
                    d[p[0]][p[1]] = distance

        # mark as visited
        v[r][c] = True
        
        # new current is lowest score
        mindist = 10000000
        current = [0,0]

        # we could search in the area of the current node to speed things up
        for p in list(edgenodes):
            # remove if already visited
            if v[p[0]][p[1]]:
                edgenodes.remove(p)  
            elif d[p[0]][p[1]] < mindist:
                current = [p[0],p[1]]
                mindist = d[p[0]][p[1]]

    print(d[nrows-1][ncols -1])
                
filename = sys.argv[1]
print(doit(filename))

