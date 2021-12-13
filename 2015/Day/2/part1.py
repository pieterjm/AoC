import re
import sys
import numpy as np

def doit(filename): 
    file = open(filename, 'r')

    s = 0
    while True:
        line = file.readline()
        line = line.rstrip().lstrip()
        if not line:
            break
        if len(line) == 0:
            break
        
        dim = [l,w,h] = line.split('x')
        [l,w,h] = [int(l),int(w),int(h)]
        opp = [l*w,w*h,h*l]
        s += 2*sum(opp) + min(opp)


    return s

        
    
filename = sys.argv[1]
print(doit(filename))


