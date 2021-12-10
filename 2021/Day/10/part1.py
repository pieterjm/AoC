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
                                        return cc[2]
        return 0


def doit(filename):
        file = open(filename, 'r')
        sumpoints = 0
        while True:
                line = file.readline()

                if not line:
                        break
                if len(line) == 0:
                        break
                line = line.rstrip().lstrip()
                
                chars = list(line)
                points = getpoints(chars)
                sumpoints = sumpoints + points
                
        return sumpoints

filename = sys.argv[1]
print(doit(filename))


