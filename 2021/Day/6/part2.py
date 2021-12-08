import re
from array import *
import sys

file = open(sys.argv[1], 'r')

line = file.readline()

numfish = [0,0,0,0,0,0,0,0,0]

fish = line.split(',')
for i in range(len(fish)):
        fish[i] = int(fish[i])
#        print(fish[i])
        numfish[fish[i]] = numfish[fish[i]] + 1
#print(numfish)
        
days = 256
while days > 0:
        temp = numfish[0]
        numfish[0] = numfish[1]
        numfish[1] = numfish[2]
        numfish[2] = numfish[3]
        numfish[3] = numfish[4]
        numfish[4] = numfish[5]
        numfish[5] = numfish[6]
        numfish[6] = numfish[7] + temp
        numfish[7] = numfish[8]
        numfish[8] = temp
#        print(numfish)
        days = days - 1

sum = 0
for i in numfish:
        sum = sum + i
print(sum)
                                
