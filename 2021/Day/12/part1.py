import re
import sys
import numpy as np

edges = {}

def findpath(path):

    solutions = 0
    loc = path[-1]
    for option in edges[loc]:
        Append = True
        if option == 'start':
            Append = False
        if option.islower() and option in path:
            Append = False

        if Append:
            path.append(option)
            if option == 'end':
                solutions += 1
            else:
                solutions += findpath(path)
            del path[-1]
        
    return solutions
        
def doit2(filename):
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
            a = m.group(1)
            b = m.group(2)

            if a in edges:
                edges[a].append(b)
            else:
                edges[a]= [b]
            if b in edges:
                edges[b].append(a)
            else:
                edges[b]= [a]

        else:
            print("problem in line: {}".format(line))
            sys.exit(0)

    return findpath(['start'])
            
    
filename = sys.argv[1]
print(doit(filename))


