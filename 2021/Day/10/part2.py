import re
import sys
import numpy as np

def getpoints(chars):
        stack = []
        for c in chars:
                if c in "{[<(":
                        stack.insert(0,c)
                else:
                        cs = stack.pop(0)
                        #print(c,cs)
                        for cc in [['(',')',3],['{','}',1197],['[',']',57],['<','>',25137]]:
                                if cs!=cc[0] and c == cc[1]:
                                        print("illegal character on detected {}".format(c))
                                        return 0

        points = 0
        for c in stack:
                for cc in [['(',1],['[',2],['{',3],['<',4]]:
                        if c == cc[0]:
                                points = points * 5
                                points += cc[1]
        return points


def doit(filename):
        file = open(filename, 'r')
        points = []
        while True:
                line = file.readline()

                if not line:
                        break
                if len(line) == 0:
                        break
                line = line.rstrip().lstrip()
                
                chars = list(line)
                print(line)

                score = getpoints(chars)
                if score > 0:
                        points.append(score)

        points.sort()
        
        return points[len(points)/2]


filename = sys.argv[1]
print(doit(filename))


