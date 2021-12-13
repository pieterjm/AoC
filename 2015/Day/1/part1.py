import re
import sys
import numpy as np

def doit(filename): 
    file = open(filename, 'r')

    line = file.readline()
    line = line.rstrip().lstrip()
    
    floor = line.count('(') - line.count(')')
    return floor    
    
    
    
filename = sys.argv[1]
print(doit(filename))


