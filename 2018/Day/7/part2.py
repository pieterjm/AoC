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
    workers = {}
    nworkers = 5
    for w in range(nworkers):
        workers[w] = {'job':'','timeleft':0}
        
    snodes = links.keys()
    snodes.sort(reverse = True)
        
    step = 0
    while True:
        log = "step: {} ".format(step)
        for w in workers:
            if workers[w]['timeleft'] == 0:
                if len(workers[w]['job']) > 0:
#                   print("Adding to solution: {}".format(workers[w]['job']))
                    solution += workers[w]['job']
                    workers[w]['job'] = ''
        for w in workers:
            if workers[w]['timeleft'] == 0:            
                # add new job                
                for node in snodes:
                    bAdd = True

                    # is already in solution
                    if node in solution:
                        bAdd = False

                    # is already running as job
                    for ww in workers:
                        if node == workers[ww]['job']:
                            bAdd = False
                            
                    # requirements are not met
                    for b in links[node]['before']:
                        if not b in solution:
                            bAdd = False
                            
                    if bAdd == True:
                        workers[w]['job'] = node
                        workers[w]['timeleft'] = ord(workers[w]['job']) - ord('A') + 61

            log += str(w) + ":" + workers[w]['job'] + " "

                    
        for w in workers:
            if workers[w]['timeleft'] > 0:
                workers[w]['timeleft'] -= 1


        print(log)

        bFinished = True
        for w in workers:
            if len(workers[w]['job']) > 0:
                bFinished = False
        if bFinished == True:
            print(solution)
            return step
                
        step += 1


filename = sys.argv[1]
print(doit(filename))


