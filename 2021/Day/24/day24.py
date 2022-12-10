import re
import sys
import numpy as np
import copy


def load(filename):
    file = open(filename, 'r')    
    program = []
    
    while True:
        line = file.readline()
        if not line:
            break
        program.append(line.strip().split(' '))
        
    return program


program = load('input.dat')

print(program)
