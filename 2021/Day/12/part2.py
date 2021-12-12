import re
import sys
import numpy as np

links = []

def findpath(path):

    solutions = 0
    loc = path[-1]
    
    options = []
    for l in links:
        if l[0] == loc:
            option = l[1]
        elif l[1] == loc:
            option = l[0]
        else:
            continue

        Append = True
        if option == 'start' and 'start' in path:
            Append = False

        if Append:
            numtwo = 0
            occ = {}
            for p in path:
                if p.islower():
                    if p in occ:
                        occ[p] += 1
                        if occ[p] == 2:
                            numtwo += 1
                            if numtwo > 1:
                                Append = False
                        elif occ[p] > 2:
                            Append = False
                    else:
                        occ[p] = 1
                        
        if Append:
            options.append(option)

    #print("options for {}".format(loc),options)
    for option in options:
        path.append(option)
        if option == 'end':
            solutions += 1
        else:
            solutions += findpath(path)
        del path[-1]
        
    return solutions
        
def doit(filename):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break
        line = line.rstrip().lstrip()
        
        
        m = re.search('^(start|end|[A-Z]+|[a-z]+)-(start|end|[A-Z]+|[a-z]+)', line)
        if m:
            links.append([m.group(1),m.group(2)])
        else:
            print("problem in line: {}".format(line))
            sys.exit(0)

    return findpath(['start'])
    
filename = sys.argv[1]
print(doit(filename))


