import re
import sys
import numpy as np


def doit(filename):
    targetx = targety = []
    
    file = open(filename, 'r')
    line = file.readline().strip()
    m = re.search("^target area: x=([0-9\-]+)\.\.([0-9\-]+), y=([0-9\-]+)\.\.([0-9\-]+)$",line)
    if m:
        targetx = [int(m.group(1)),int(m.group(2))]
        targety = [int(m.group(3)),int(m.group(4))]
    else:
        print("no match")
        sys.exit(0)

    # max horizontal steps

    hits = {}

    minvx = 1
    maxvx = targetx[1]
    minvy = min(targety[0],targety[1])
    maxvy = -1 * minvy
    
    for vx in range(1 + maxvx - minvx):
        vx += minvx
        vxs = vx
        for vy in range(1 + maxvy - minvy):
            vy += minvy
            vx = vxs
            vys = vy
            pos = [0,0]

            bCont = True
            while bCont:
                pos[0] += vx
                if vx > 0:
                    vx -= 1
                pos[1] += vy
                vy -= 1

                if targetx[0] <= pos[0] <= targetx[1] and targety[0] <= pos[1] <= targety[1]:
                    bCont = False
                    print("hit the target",pos,vxs,vys)
                    key = "{},{}".format(vxs,vys)
                    if key in hits:
                        hits[key] += 1
                    else:
                        hits[key] = 1
                elif pos[1] < min(targety):
                    bCont = False
                    
    return len(hits)
    

filename = sys.argv[1]
print(doit(filename))


