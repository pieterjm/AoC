import re
from array import *
import sys

def calcfuel(pos, t):
        fuel = 0
        for p in pos:
                steps = abs(p-t)
                while steps > 0:
                        fuel = fuel + steps
                        steps = steps - 1
	return fuel


def doit(filename):
	file = open(filename, 'r')

	line = file.readline()

	pos = line.split(',')
	for i in range(len(pos)):
        	pos[i] = int(pos[i])
        
	sum = 0
	n = 0
	for p in pos:
	        n = n + 1
	        sum = sum + p

	avg = int(sum / n)

	minfuel = calcfuel(pos,avg-5)
	for a in range(avg-5,avg+5):
		fuel = calcfuel(pos,a)
		if fuel < minfuel:
			minfuel = fuel
	return minfuel

filename = sys.argv[1]		
print("filename: {}, minfuel: {}".format(filename,doit(filename)))
