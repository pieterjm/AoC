import re
import sys
import numpy as np

def doit(filename): 
    file = open(filename, 'r')

    s = 0
    r = 0
    while True:
        line = file.readline()
        line = line.rstrip().lstrip()
        if not line:
            break
        if len(line) == 0:
            break
        
        [l,w,h] = line.split('x')
        dim = [l,w,h] = [int(l),int(w),int(h)]
        opp = [l*w,w*h,h*l]
        s += 2*sum(opp) + min(opp)

        dim.remove(max(dim))
        r += l*w*h + 2*(dim[0]+dim[1]) 
        
    return r

        
    
filename = sys.argv[1]
print(doit(filename))


