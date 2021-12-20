from math import cos, sin
import re
import sys
import numpy as np


def rotate(p,idx):
    rots = [-1*p[2],-1*p[0],p[1]],[-1*p[2],p[1],p[0]],[-1*p[2],p[0],-1*p[1]],[-1*p[2],-1*p[1],-1*p[0]],[-1*p[1],p[2],-1*p[0]],[-1*p[1],-1*p[2],p[0]],[-1*p[1],-1*p[0],-1*p[2]],[-1*p[1],p[0],p[2]],[-1*p[0],-1*p[2],-1*p[1]],[-1*p[0],-1*p[1],p[2]],[-1*p[0],p[1],-1*p[2]],[-1*p[0],p[2],p[1]],[p[0],-1*p[2],p[1]],[p[0],p[1],p[2]],[p[0],p[2],-1*p[1]],[p[0],-1*p[1],-1*p[2]],[p[1],p[2],p[0]],[p[1],-1*p[2],-1*p[0]],[p[1],-1*p[0],p[2]],[p[1],p[0],-1*p[2]],[p[2],p[1],-1*p[0]],[p[2],p[0],p[1]],[p[2],-1*p[0],-1*p[1]],[p[2],-1*p[1],p[0]]
    return [rots[idx][0],rots[idx][1],rots[idx][2]]

def doit(filename):
    scanners = {}
    scannerid = None
    file = open(filename, 'r')    
    while True:
        line = file.readline()
        if not line:
            break
        line = line.strip()
        m = re.search("^--- scanner (\d+) ---$",line)        
        if m:
            print(m.group(1))
            scannerid = int(m.group(1))
            scanners[scannerid] = {"probes":[],"done":False}
        else:
            probe = line.split(",")
            if len(probe) == 3:
                scanners[scannerid]['probes'].append([int(probe[0]),int(probe[1]),int(probe[2])])

    # create a list of probes where all probes as seen by scanner 1 are stored
    probes = {}
    for p in scanners[0]['probes']:
        probes[repr(p)] = p
        
    print(len(probes))


    
    # iterate over all other scanners
    cont = True
    while cont:
        cont = False
        for scannerid in range(1,len(scanners)):
            if scanners[scannerid]['done'] == False:
                cont = True
                print("scanner",scannerid)


                # try all orientations of p1
                for ri in range(24):
                    # this is the dataset we are working on
                    ps = []
            
                    # create base dataset for this rotation
                    for p1 in scanners[scannerid]['probes']:
                        ps.append(rotate(p1,ri))

                
                    # iterate over all probes in scanner 0, set this to the center
                    for p0 in probes.values():
                        for p1 in ps:

                            # we assume that p0 and p1 have the same position
                            # we transpose all other points of scannerid with this vector
                            t = [0,0,0]
                            for d in range(3):
                                t[d] = p0[d] - p1[d]                    

                            # now count how many probes are overlapping for this rotation and this transposition
                            numsame = 0
                            for p2 in ps:
                                p3 = [0,0,0]
                                for d in range(3):
                                    p3[d] = p2[d] + t[d] 

                                if repr(p3) in probes:
                                    numsame += 1
#                                for p4 in probes.values():
#                                    if p4[0] == p3[0] and p4[1] == p3[1] and p4[2] == p3[2]:
#                                        numsame += 1
                            
                            
                            if numsame >= 12 and scanners[scannerid]['done'] == False:
                                scanners[scannerid]['done'] = True
                                print("Rotation correct",ri)
                                for p2 in ps:
                                    p3 = [0,0,0]
                                    for d in range(3):
                                        p3[d] = p2[d] + t[d]


                                    probes[repr(p3)] = p3
                                print("num probes",len(probes))
    print(len(probes))
    print(probes)
    return 0
                
filename = sys.argv[1]
print(doit(filename))


