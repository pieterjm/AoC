import re
from array import *
import sys

def overlap(s1,s2):
        num = 0
        if len(s1) == 0:
                print("string len is 0!!!!")
                sys.exit()
        for c in list(s1):
                if c in list(s2):
                        num = num + 1
        return num

def doit(filename):
	file = open(filename, 'r')

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


                if ( numlow == 4 ):
                    sumlow += grid[r][c] + 1
                                                                  
        return sumlow

filename = sys.argv[1]
print(doit(filename))


