import re
import sys
import numpy as np

def doit(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = list(lines[i].rstrip().lstrip())
    numlines = len(lines)
        
    for i in range(numlines):
        linelen = len(lines[i])
        for j in range(i+1,numlines):
            
            num = 0
            solution = ""
            for k in range(linelen):                
                if lines[i][k] != lines[j][k]:
                    num += 1
                else:
                    solution += lines[i][k]
            if num == 1:
                return solution

    
filename = sys.argv[1]
print(doit(filename))


