import re
import sys
import numpy as np

s = 0

def parse(i,binary):
    istart = i
    global s
    
    version = int(binary[i:i+3],2)
    s += version
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
    else:  #operator packet
        lti = int(binary[i:i+1],2)
        i += 1
        print("length type indicator  = {}".format(lti))

        if lti == 0: # total length in bits
            tl = int(binary[i:i+15],2)
            i += 15
            print("Total length = {}".format(tl))
            
            di = i + tl
            while i < di:
                # parse subpackets
                i += parse(i,binary)
        else: # number of packets
            n = int(binary[i:i+11],2)
            i += 11
            for j in range(n):
                i += parse(i,binary)
    return (i - istart)

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

    parse(0,binary)

    global s
    print(s)

                
filename = sys.argv[1]
print(doit(filename))


