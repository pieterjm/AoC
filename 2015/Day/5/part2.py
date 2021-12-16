import re
import sys
import numpy as np
import hashlib

def doit(filename): 
    file = open(filename, 'r')
    

    nice = 0
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break
        line = line.strip()


        n = 0
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                n = 1

        if n > 0:
            n = 0
            for i in range(len(line)-1):
                pair1 = line[i] + line[i+1]
                for j in range(len(line)-1):
                    if j + 1 < i or j > i + 1:
                        pair2 = line[j] + line[j+1]
                        if pair1 == pair2:
                            n = 1
            nice += n
        
    return nice
    
filename = sys.argv[1]
print(doit(filename))


