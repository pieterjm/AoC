import re
import sys
import numpy as np

def doit(filename):
    file = open(filename, 'r')

    
    oline = file.readline()
    
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    minlen = len(oline)
    for c in alphabet:
        line = oline.replace(c,"").replace(c.upper(),"")

        cont = True
        while cont:            
            linelen = len(line)
            for cc in list('abcdefghijklmnopqrstuvwxyz'):            
                p1 = cc + cc.upper()
                p2 = cc.upper() + cc
                line = line.replace(p1,"")
                line = line.replace(p2,"")
                
            if len(line) == linelen:
                if linelen < minlen:
                    minlen = linelen
                cont = False
    return minlen
                    
filename = sys.argv[1]
print(doit(filename))


