import re
import sys
import numpy as np


def parse(i,binary):
    print("Start parsing a packet")
    istart = i # record the startpointer of the packet

    # get version and type
    version = int(binary[i:i+3],2)
    typeid = int(binary[i+3:i+6],2)    
    i += 6
    print("version = {}".format(version))
    print("typeid  = {}".format(typeid))

    if typeid == 4: #literal value packet
        n = ""
        keepreading = True
        while keepreading:
            l = int(binary[i],2)
            i += 1

            n += binary[i:i+4]
            i += 4

            if l == 0:
                keepreading = False
        n = int(n,2)
        print("literal value = {}".format(n))

        # return the number of bits we progressed and the value
        return (i-istart),n,version
        
    else:  #operator packet
        lti = int(binary[i:i+1],2)
        i += 1
        print("length type indicator  = {}".format(lti))

        vals = []
        if lti == 0: # total length is in 15 bits
            tl = int(binary[i:i+15],2)
            i += 15
            print("Total length = {}".format(tl))
            
            di = i + tl
            while i < di:
                # parse subpackets
                ii,v,vs = parse(i,binary)
                vals.append(v)
                i += ii
                version += vs
                
        else: # total length is the number of packets in 11 bits
            n = int(binary[i:i+11],2)
            i += 11            
            for j in range(n):
                ii,v,vs = parse(i,binary)
                i += ii
                vals.append(v)
                version += vs

        m = 0
        if typeid == 0: # sum values
            m = sum(vals)            
        elif typeid == 1: # multiply all values
            m = vals[0]
            for j in range(1,len(vals)):
                m *= vals[j]
        elif typeid == 2: # minimum value
            m = min(vals)
        elif typeid == 3: # maximum value
            m = max(vals)            
        elif typeid == 5: # first value is greater
            if vals[0] > vals[1]:
                m = 1                
            else:
                m = 0                
        elif typeid == 6: # first value is smaller
            if vals[0] < vals[1]:
                m = 1                
            else:
                m = 0
        elif typeid == 7: # values are equal
            if vals[0] == vals[1]:
                m = 1
            else:
                m = 0
        else:
            print("unknown typeid {}".format(typeid))
            sys.exit(0)
                  
        return (i - istart),m,version


def doit(filename):
    tobits = {
        '0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'
    }


    
    file = open(filename, 'r')
    data = list(file.readline().strip())
    binary = ""
    for i in data:
        binary += tobits[i]
        
    i,v,s = parse(0,binary)

    print("Sum of all versions = {}".format(s))
    print("Total value = {}".format(v))
    
    return v


                
filename = sys.argv[1]
print(doit(filename))


