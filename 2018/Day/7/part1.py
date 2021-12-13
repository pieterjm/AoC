import re
import sys
import numpy as np

def doit(filename):
    file = open(filename, 'r')

    links = {}
    
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break

        m = re.search("^Step (\S+) must be finished before step (\S+) can begin\.$",line)
        if m:
            before = m.group(1)
            after = m.group(2)

            if after not in links:
                links[after] = {'before': [], 'after': []}                
            links[after]['before'].append(before)
            if before not in links:
                links[before] = {'before': [], 'after': []}                
            links[before]['after'].append(after)
        else:
            print("Error",line)
            sys.exit(0)



    
    # find the start node
    nodes = []
    for node in links:
        if len(links[node]['before']) == 0:
            nodes.append(node)
    nodes.sort()
    print(nodes)

    solution = ""
    available = nodes

    while True:
        available.sort( reverse=True)

        if len(available) == 0:
            return solution
        
        node = available.pop()

        bDone = True
        if node in solution:
            bDone = False
        for i in links[node]['before']:
            if not i in solution:
                bDone = False
        if bDone:
            solution += node

        for i in links[node]['after']:
            if not i in solution:
                available.append(i)
                
            
            
    return -1


filename = sys.argv[1]
print(doit(filename))


