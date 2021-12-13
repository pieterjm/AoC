import re
import sys
import numpy as np

def printpaper(paper):
    for row in paper:
        print("".join(row))

def doit(filename):
    file = open(filename, 'r')

    dots = []
    paper = []
    instructions = []

    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:            
            break

        line = line.rstrip().lstrip()
        m = re.search("^(\d+),(\d+)$",line)
        if m:
            dots.append([int(m.group(1)),int(m.group(2))])
            continue

        m = re.search("^fold along (x|y)=(\d+)$",line)
        if m:
            instructions.append([m.group(1),int(m.group(2))])
            continue

    maxx = 0
    maxy = 0
    for dot in dots:
        if dot[0] > maxx:
            maxx = dot[0]
        if dot[1] > maxy:
            maxy = dot[1]
    maxx += 1
    maxy += 1
            
    print("maxx = {}, maxy = {}".format(maxx,maxy))
    paper = []
    for x in range(maxx):
        row = []
        for y in range(maxy):
            row.append(".")
        paper.append(row)


    for dot in dots:
        print(dot)
        paper[dot[0]][dot[1]] = "#"

    printpaper(paper)

    for instruction in instructions:
        newpaper = []
        if instruction[0] == 'y':
            maxy = instruction[1]
        elif instruction[0] == 'x':
            maxx = instruction[1]

        numdots = 0
        for x in range(maxx):
            row = []
            for y in range(maxy):
                if instruction[0] == 'x' and (paper[x][y] == '#' or paper[instruction[1]*2 - x][y] == '#'):
                    row.append("#")
                    numdots += 1
                elif instruction[0] == 'y' and (paper[x][y] == '#' or paper[x][instruction[1]*2 - y] == '#'):
                    row.append("#")
                    numdots += 1
                else:
                    row.append(".")
                
            newpaper.append(row)
            
        print("finished folding {} dots".format(numdots))
        return numdots
        printpaper(newpaper)

        paper = newpaper
            
    return -1
            
    
filename = sys.argv[1]
print(doit(filename))


