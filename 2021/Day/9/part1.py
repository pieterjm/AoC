import re
import sys
import numpy as np

def doit(filename):
        file = open(filename, 'r')
        sumlow = 0
        nrows = 0
        ncols = 0
        grid = []
        while True:
            line = file.readline()                
            if not line:
                break
            if len(line) == 0:
                break

            nrows = nrows + 1
            row = list(line.rstrip())
            ncols = len(row)
            for r in range(ncols):
                row[r] = int(row[r])
            

            grid.append(row)

        grid = np.array(grid)
        grid = np.insert(grid,0,np.array([9] * ncols),0)
        grid = np.insert(grid,nrows + 1,np.array([9] * ncols),0)
        grid = np.insert(grid,0,np.array([9] * (nrows + 2)),1)
        grid = np.insert(grid,ncols + 1,np.array([9] * (nrows + 2)),1)

        for r in range(1,1 + nrows):
                for c in range(1,1 + ncols):
                        if (grid[(r,c-1)] > grid[(r,c)] and
                            grid[(r,c+1)] > grid[(r,c)] and
                            grid[(r-1,c)] > grid[(r,c)] and
                            grid[(r+1,c)] > grid[(r,c)]):
                                sumlow += 1 + grid[(r,c)]
        return sumlow

filename = sys.argv[1]
print(doit(filename))


