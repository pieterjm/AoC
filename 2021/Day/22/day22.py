import re
import sys
import numpy as np
import copy

def load(filename):
    file = open(filename, 'r')    

    instructions = []
    while True:
        line = file.readline()
        if not line:
            break
        
        line = line.strip()

        m = re.search("^(on|off) x=([\-0-9]+)\.\.([\-0-9]+),y=([\-0-9]+)\.\.([\-0-9]+),z=([\-0-9]+)\.\.([\-0-9]+)$",line)
        if m:                        
            instructions.append({
                'on': m.group(1) == 'on',
                'dim': [int(m.group(2)),int(m.group(4)),int(m.group(6)),int(m.group(3))+1,int(m.group(5))+1,int(m.group(7))+1],
                'x': [int(m.group(2)),int(m.group(3))],
                'y': [int(m.group(4)),int(m.group(5))],
                'z': [int(m.group(6)),int(m.group(7))]
                })
        else:
            print("Could not parse line: ",line)
            sys.exit(0)

    return instructions


def part1(instructions):
    lights = {}
    for i in instructions:
        if i['x'][0] >= -50 and i['x'][1] <= 50:
            for x in range(i['x'][0],i['x'][1]+1):
                if i['y'][0] >= -50 and i['y'][1] <= 50:
                    for y in range(i['y'][0],i['y'][1]+1):
                        if i['z'][0] >= -50 and i['z'][1] <= 50:
                            for z in range(i['z'][0],i['z'][1]+1):
                                key = repr([x,y,z])
                                if i['on'] == True:
                                    lights[key] = 1
                                elif key in lights:
                                    del lights[key]
    return len(lights)


def volume(dim):
    v = 1
    for d in range(3):
        v *= (abs(dim[d+3] - dim[d]))
    return v

def intersection(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    zA = max(boxA[2], boxB[2])    
    xB = min(boxA[3], boxB[3])
    yB = min(boxA[4], boxB[4])
    zB = min(boxA[5], boxB[5])

    # compute the area of intersection rectangle
    interArea = abs(max((xB - xA, 0)) * max((yB - yA), 0) * max((zB - zA),0))
    if interArea == 0:
        return 0, []
    else:
        interArea =  (abs(xB - xA)) * (abs(yB - yA)) * (abs(zB - zA))
        
    return interArea, [xA,yA,zA,xB,yB,zB]

def part2(instructions):
    lights = []
    numon = 0
    numoff = 0
    

    # iterate over all instructions
    for i in instructions:
        # iterate over all previous instructions
        l = len(lights)
        for jc in range(l):
            j = lights[jc]
            
            # calculate overlap
            intr, dim = intersection(i['dim'],j['dim'])

            # if it is on and no overlap
            if intr > 0:
                if i['on'] == True and j['on'] == True:
                    lights.append({'on':False,'dim':list(dim)})
                    numoff += volume(dim)
                elif i['on'] == True and j['on'] == False:
                    lights.append({'on':True,'dim':list(dim)})
                    numon += volume(dim)
                elif i['on'] == False and j['on'] == True:
                    lights.append({'on':False,'dim':list(dim)})
                    numoff += volume(dim)
                elif i['on'] == False and j['on'] == False:
                    lights.append({'on':True,'dim':list(dim)})
                    numon += volume(dim)

                
        if i['on'] == True:
            lights.append({'on':i['on'],'dim':list(i['dim'])})
            numon += volume(i['dim'])

    return numon - numoff

        
assert(part1(load('sample.dat')) == 39)
assert(part1(load('sample2.dat')) == 590784)
assert(part1(load('sample3.dat')) == 474140)

print("Solution for part 1 = {}".format(part1(load('input.dat'))))
assert(part2(load('sample3.dat')) == 2758514936282235)
print("Solution for part 2 = {}".format(part2(load('input.dat'))))



