import re
import sys
import numpy as np
    
def doit(filename):
    global freqmax, freqmin
    file = open(filename, 'r')

    # read start sequence
    sequence = file.readline()
    sequence = sequence.lstrip().rstrip()
    file.readline() # read empty line

    # read rules
    rules = {}
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:            
            break

        line = line.rstrip().lstrip().split(" ")
        rules[line[0]] = line[2]

    # really creating the sequence by inserting characters according
    # to the result will make the program so slow that finding the
    # solution will simply take very long.
    # That is not required as we can split up the sequence in distinct
    # pairs and track the amount of pairs in the sequence. In each step
    # each pair is destroyed and creates two new pairs. As such all the
    # same pairs in the sequence are processed in one go

    # split the sequnce up into seperate pairs and count how many there are
    pairs = {}
    for i in range(len(sequence)-1):
        pair = sequence[i] + sequence[i+1]
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1

    # do forty steps
    for step in range(40):

        # create a new dictionary of the pairs and their amount
        newpairs = {}
        for pair in pairs:
            # each pair is split into two new pairs
            for p in [pair[0]+rules[pair],rules[pair]+pair[1]]:

                # add the count number of new pairs 
                if p in newpairs:
                    newpairs[p] += pairs[pair]
                else:
                    newpairs[p] = pairs[pair]

        # swap the dictionary
        pairs = newpairs.copy()

        
        print(step,sum(pairs.values())+1)

    # calculate the frequency of all letters
    freq = {}
    for pair in pairs:

        # take the first letter of each pair
        c = pair[0]
        if c in freq:
            freq[c] += pairs[pair]
        else:
            freq[c] = pairs[pair]

    # add the last letter of the sequence as it is not in a pair
    freq[sequence[-1]] += 1

    # calculate the difference between the maximum and the minimum
    return (max(freq.values())-min(freq.values()))
    
filename = sys.argv[1]
print(doit(filename))


