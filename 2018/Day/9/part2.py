import re
import sys
import numpy as np

i = 0

def printmarbles(step,marbles):
    line = "[{}] ".format(step + 1)

    mid = 0
    while True:
        line += str(mid) + " "
        mid = marbles[mid]['cw']
        if mid == 0:
            print(line)
            return
    
        
def doit(filename): 
    file = open(filename, 'r')
    line = file.readline()
    line = line.rstrip().lstrip()

    nplayers = 1
    lastmarble = 0
    
    m = re.search("^(\d+) players; last marble is worth (\d+) points$",line)
    if m:
        nplayers = int(m.group(1))
        lastmarble = int(m.group(2)) * 100

    
    marbles = {
        0:{'cw':0,'ccw':0}
    }

    current = 0
    mid = 0

    score = [0] * nplayers
    pid = 0
    while mid < lastmarble:
        mid += 1
    
        if mid % 23 == 0:
            score[pid] += mid
            rid = current
            for i in range(7):
                rid = marbles[rid]['ccw']
            score[pid] += rid

            marbles[marbles[rid]['ccw']]['cw'] = marbles[rid]['cw']
            marbles[marbles[rid]['cw']]['ccw'] = marbles[rid]['ccw']
            current = marbles[rid]['cw']
        else:
            # insert the new marble
            marbles[mid] = {
                'ccw':marbles[current]['cw'],
                'cw':marbles[marbles[current]['cw']]['cw']
            }

            # link the cw and ccw marbles
            marbles[marbles[mid]['cw']]['ccw'] = mid
            marbles[marbles[mid]['ccw']]['cw'] = mid
        
            current = mid
        #printmarbles(pid,marbles)

        pid += 1
        if pid == nplayers:
            pid = 0
    return max(score)
    
filename = sys.argv[1]
print(doit(filename))


