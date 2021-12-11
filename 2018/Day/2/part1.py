import re
import sys
import numpy as np

def doit(filename):
    file = open(filename, 'r')
    
    snum = [0,0,0,0,0]
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break
        line = line.rstrip().lstrip()

        freq= {}
        chars = list(line)
        for char in chars:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1


        num = [0 for i in range(len(chars))]        
        for char in freq:
            num[freq[char]] += 1

        if ( num[2] > 0 ):
            snum[2] += 1
        if ( num[3] > 0):
            snum[3] += 1

        
    return snum[2]*snum[3]
    
filename = sys.argv[1]
print(doit(filename))


