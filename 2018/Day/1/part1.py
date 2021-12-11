import re
import sys
import numpy as np

def doit(filename):
        file = open(filename, 'r')

        sum = 0
        
        while True:
                line = file.readline()
                if not line:
                        break
                if len(line) == 0:
                        break
                sum += int(line)

        return sum
    
filename = sys.argv[1]
print(doit(filename))


