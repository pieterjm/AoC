import re
from array import *
import sys


def doit(filename):
	file = open(filename, 'r')


        num = 0
        while True:
                line = file.readline()                
                if not line:
                        break
                line = line.rstrip()
	        [testdata,data]= line.split('|')
                segments = data.split(' ')
                for s in segments:
                        if ((len(s) == 2)or(len(s)==3)or(len(s)==4)or(len(s)==7)):
                                num = num + 1
        return num


filename = sys.argv[1]
print("Filename: {}, Sum: {}".format(filename,doit(filename)))


