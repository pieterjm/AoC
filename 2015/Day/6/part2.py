import re
import sys
import numpy as np
import hashlib

def doit(filename): 
    # create and initialize grid
    grid = []
    for r in range(1000):
        row = []
        for c in range(1000):
            row.append(0)
        grid.append(row)

    # read instructions
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break
        line = line.strip()

        m = re.search("^(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)$",line)
        if m:
            command = m.group(1)
            start = [int(m.group(2)),int(m.group(3))]
            stop = [int(m.group(4)),int(m.group(5))]
        else:
            print("could not parse line:",line)
            sys.exit(0)

        # iterate through the block
        for r in range(start[0],stop[0] + 1):
            for c in range(start[1],stop[1] + 1):
                if command == 'toggle':
                    grid[r][c] += 2
                elif command == 'turn on':
                    grid[r][c] += 1
                elif command == 'turn off':
                    if grid[r][c] > 0:
                        grid[r][c] -= 1
                else:
                    print("unknown command: ",command)
                    sys.exit(0)

    num = 0
    for r in range(1000):
        for c in range(1000):
            num += grid[r][c]
            
    return num
            
            
    
filename = sys.argv[1]
print(doit(filename))


