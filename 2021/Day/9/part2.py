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
        if c > 0 and grid[r][c-1] < 9 and notinbasin(basin,r,c-1):
            checklist.append([r,c-1])
        if c + 1 < ncols and grid[r][c+1] < 9 and notinbasin(basin,r,c+1):        
            checklist.append([r,c+1])
        if r > 0 and grid[r-1][c] < 9 and notinbasin(basin,r-1,c):
            checklist.append([r-1,c])
        if r + 1 < nrows and grid[r+1][c] < 9 and notinbasin(basin,r+1,c):        
            checklist.append([r+1,c])

    
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
                if (c == 0 ):
                    numlow = numlow + 1
                elif grid[r][c] < grid[r][c -1]:
                    numlow = numlow + 1
                if (c == ncols -1):
                    numlow = numlow + 1
                elif grid[r][c] < grid[r][c  + 1]:
                    numlow = numlow + 1
                if (r == 0):
                    numlow = numlow + 1
                elif grid[r][c] < grid[r-1][c]:
                    numlow = numlow + 1
                if (r + 1 == nrows):
                    numlow = numlow + 1
                elif grid[r][c] < grid[r+1][c]:
                    numlow = numlow + 1
#                print(r,c,grid[r][c],numlow)

                if ( numlow == 4 ):
                    sumlow += grid[r][c] + 1

                    size = calcbasinsize(grid,nrows,r,ncols,c)
                    basins.append(size)

        basins.sort(reverse=True)
        return basins[0]*basins[1]*basins[2]

filename = sys.argv[1]
print(doit(filename))


