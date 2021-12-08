import re
from array import *
import sys

file = open(sys.argv[1], 'r')

line = file.readline()

fish = line.split(',')
for i in range(len(fish)):
        fish[i] = int(fish[i])

for d in range(80):
        lf = len(fish)
        for i in range(lf):
                if fish[i] == 0:
                        fish[i] = 6
                        fish.append(8)
                else:
                        fish[i] = fish[i] - 1

print(len(fish))
                                
