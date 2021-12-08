import re
from array import *
import sys

def calcfuel(pos,p):
        fuel = 0
        for t in pos:
                fuel = fuel + abs(t - p)
#        print("position {}, fuel {}".format(p,fuel))
        return fuel
        
def doit(filename):
	file = open(filename, 'r')

	line = file.readline()

	pos = line.split(',')
	for i in range(len(pos)):
        	pos[i] = int(pos[i])
        

	max = 0
	min = 0
	for p in pos:
        	if p > max:
                	max = p
	        if p < min:
        	        min = p

	minfuel = -1
	for t in range(min,max+1):
        	fuel = 0
        	for p in pos:
                	fuel = fuel + abs(p - t)
        	if ((fuel < minfuel)or(minfuel<0)):
                	minfuel = fuel

	return minfuel

filename = sys.argv[1]
print("Solution: {}".format(doit(filename)))



