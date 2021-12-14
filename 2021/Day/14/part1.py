import re
import sys
import numpy as np

def doit(filename):
    file = open(filename, 'r')

        
    sequence = file.readline()
    sequence = sequence.lstrip().rstrip()
    file.readline() # read empty line
    rules = {}
    
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:            
            break

        line = line.rstrip().lstrip().split(" ")
        rules[line[0]] = line[2]
    print(rules)
    
    for s in range(10):
        i = 0
        while i < len(sequence) - 1:
            pair = sequence[i] + sequence[i+1]
            if pair in rules:
                i += 1
                sequence = sequence[:i] + rules[pair] + sequence[i:]
            i += 1

    freq = {}
    for c in list(sequence):
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    print(freq)
    maxf = sequence[0]
    minf = sequence[0]
    for c in freq:
        if freq[c] < freq[minf]:
            minf = c
        if freq[c] > freq[maxf]:
            maxf = c


    return (freq[maxf] - freq[minf])
            
    
filename = sys.argv[1]
print(doit(filename))


