import re
import sys
import numpy as np

rules = {}
freq = {}
stepl = 0

def runner(pair, step):
    global rules, freq, stepl

    stepl += 1
    if stepl % 10000000 == 0:
        print(stepl)

    if step == 0:
        return 0

    freq[rules[pair]] += 1
    
    l = runner(pair[0] + rules[pair], step - 1)
    l += runner(rules[pair] + pair[1], step - 1)
    return l + 1
    
    
def doit(filename):
    global freqmax, freqmin
    file = open(filename, 'r')

        
    sequence = file.readline()
    sequence = sequence.lstrip().rstrip()
    file.readline() # read empty line
    global rules
    rules = {}
    
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:            
            break

        line = line.rstrip().lstrip().split(" ")
        rules[line[0]] = line[2]

    global freq

    freq = {}
    freqs = {}
    for pair in rules:
        for c in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            freq[c] = 0    
        l = runner(pair, 24)
        for c in list(freq):
            if freq[c] == 0:
                del freq[c]
        freqs[pair] = freq.copy()

    print("first part done", stepl)
    
    sfreq = {}        
    for c in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        sfreq[c] = 0

        
    for s in range(16):
        print(s)
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


        
        
    for i in range(len(sequence)-1):
        pair = sequence[i] + sequence[i+1]
        for c in freqs[pair]:
            sfreq[c] += freqs[pair][c]
    for c in sequence:
        sfreq[c] += 1

            
    for c in list(sfreq):
        if sfreq[c] == 0:
            del sfreq[c]


    
    print(max(sfreq.values()) - min(sfreq.values()))
            
filename = sys.argv[1]
print(doit(filename))


