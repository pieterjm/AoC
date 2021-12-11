import re
import sys
import numpy as np

def doit(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    sum = 0
    freq = {}
        
    while True:
        for line in lines:
            line = line.rstrip().lstrip()
            sum += int(line)
            
            if str(sum) in freq:
                return sum
            
            freq[str(sum)] = 1
            
filename = sys.argv[1]
print(doit(filename))


