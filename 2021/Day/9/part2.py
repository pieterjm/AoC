import re
from array import *
import sys

def notinbasin(basin,r,c):
    for [br,bc] in basin:
        if br == r and bc == c:
            return False
    return True
    
def calcbasinsize(grid,nrows,r,ncols,c):
    # als neighbour = 9, stop
    
    checklist = [[r,c]]
    basin = []
    checked = []
    
    size = 0
    count = 0
    while len(checklist) > 0:
        count = count + 1

        
        [r,c] = checklist.pop(0)
        if grid[r][c] == 9:
            print("Got a nine!!")
            sys.exit()


        if notinbasin(basin,r,c):            
            basin.append([r,c])
            size = size + 1

            
        # check all neighbours
        for [i,j] in [[r,c-1],[r,c+1],[r-1,c],[r+1,c]]:
            if 0 <= i < nrows and 0 <= j < ncols:
                if notinbasin(basin,i,j):
                    if grid[i][j] < 9:
                        checklist.append([i,j])
    
    return size
    

    

def doit(filename):
	file = open(filename, 'r')
        basins = []
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


        sumlow = 0


        for r in range(nrows):
            for c in range(ncols):

                numlow = 0

                for [i,j] in [[r,c-1],[r,c+1],[r-1,c],[r+1,c]]:
                    if 0 <= i < nrows and 0 <= j < ncols:
                        if grid[r][c] < grid[i][j]:
                            numlow += 1
                    else:
                        numlow += 1    


                if ( numlow == 4 ):
                    sumlow += grid[r][c] + 1
                    size = calcbasinsize(grid,nrows,r,ncols,c)
                    basins.append(size)

        basins.sort(reverse=True)
        return basins[0]*basins[1]*basins[2]

filename = sys.argv[1]
print(doit(filename))


