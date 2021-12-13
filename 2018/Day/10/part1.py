import re
import sys
import numpy as np

def printimage(points):
    maxx = minx = points[0]['position'][0]
    maxy = miny = points[0]['position'][1]
    for point in points:
        minx = min([point['position'][0],minx])
        maxx = max([point['position'][0],maxx])
        miny = min([point['position'][1],miny])
        maxy = max([point['position'][1],maxy])
    maxx += 1
    maxy += 1

    grid = []
    for y in range(miny,maxy):
        line = []
        for x in range(minx,maxx):
            line.append(".")
        grid.append(line)
        
    for point in points:
        grid[point['position'][1] - miny][point['position'][0] - minx] = '#'

    for line in grid:
        print("".join(line))

def doit(filename): 
    file = open(filename, 'r')


    points = []
    while True:
        line = file.readline()
        line = line.rstrip().lstrip()
        if not line:
            break
        if len(line) == 0:
            break
        
        parts = re.split("=|<|>|,",line)

        points.append({
            'position':[int(parts[2]),int(parts[3])],
            'velocity':[int(parts[6]),int(parts[7])]
        })


        

    # move the points
    width = prevwidth = 0
    step = 0
    while True:
        # calculate the width of the image
        maxy = miny = points[0]['position'][1]
        for point in points:
            miny = min([point['position'][1],miny])
            maxy = max([point['position'][1],maxy])
        prevwidth = width
        width = abs(maxy - miny)
        if prevwidth != 0 and width > prevwidth:
            for point in points:
                for d in range(2):
                    point['position'][d] -= point['velocity'][d]
            step -= 1
            break
        
        # make a step
        for point in points:
            for d in range(2):
                point['position'][d] += point['velocity'][d]
        step += 1

    printimage(points)
    return step
    
filename = sys.argv[1]
print(doit(filename))


