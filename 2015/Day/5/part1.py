import re
import sys
import numpy as np
import hashlib

def doit(filename): 
    file = open(filename, 'r')

    vowels = list('aeiou')
    dble   = []
    for c in list('abcdefghijklmnopqrstuvwxyz'):
        dble.append(c + c)
    ncont  = ['ab','cd','pq','xy']
    print(dble)
    nice = 0
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break
        line = line.strip()


        n = 0
        print(line)
        for p in ncont:
            if p in line:
                print("disallowed pattern {} in line".format(p))
                n += 1
        if n == 0:
            for p in dble:
                if p in line:
                    n += 1
            print("Number of doubles {}".format(n))
            if n > 0:
                n = 0
                for p in vowels:
                    n += line.count(p)
                if n > 2:
                    nice += 1
    return nice
    
filename = sys.argv[1]
print(doit(filename))


