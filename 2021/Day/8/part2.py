import re
from array import *
import sys

def overlap(s1,s2):
        num = 0
        if len(s1) == 0:
                print("string len is 0!!!!")
                sys.exit()
        for c in list(s1):
                if c in list(s2):
                        num = num + 1
        return num

def doit(filename):
	file = open(filename, 'r')
        
        sum = 0
        while True:
                
                line = file.readline()                
                if not line:
                        break
                if len(line) == 0:
                        break
                
                segments = {
                        'a':['a','b','c','d','e','f','g'],
                        'b':['a','b','c','d','e','f','g'],
                        'c':['a','b','c','d','e','f','g'],
                        'd':['a','b','c','d','e','f','g'],
                        'e':['a','b','c','d','e','f','g'],
                        'f':['a','b','c','d','e','f','g'],
                        'g':['a','b','c','d','e','f','g']
                        }
     
                
                line = line.rstrip()
	        [testdata,data]= line.split('|')
                testdata = testdata.lstrip().rstrip().split(' ')
                data = data.lstrip().rstrip().split(' ')
                # data is also testdata
                testdata.extend(data)

                #1 cf
                #7 acf
                #4 bcdf

                #2 acdeg  1:1, 7:2,  4:2
                #3 acdfg  1:2, 7:3,  4:3
                #5 abdfg  1:1  7:2   4:3

                #6 abdefg 1:1  7:2 4:3
                #0 abcefg 1:2  7:3 4:3
                #9 abcdfg 1:2  7:3 4:4

                #8 abcdefg

                # learn the digits

                mapping = [[],[],[],[],[],[],[],[],[],[]]
                for d in testdata:
                        d = ''.join(sorted(d))
                        l = len(d)
                        
                        if l == 2:
                                mapping[1] = d
                        elif l == 3:
                                mapping[7] = d
                        elif l == 4:
                                mapping[4] = d
#                print(mapping)
                                

                # get digits from data
                factor = 1000
                subsum = 0
                for d in data:
                        digit = -1
                        d = ''.join(sorted(d))
                        l = len(d)
                        if l == 2:
                                digit = 1                                
                        elif l == 3:
                                digit = 7
                        elif l == 4:
                                digit = 4
                        elif l == 5: # 2 3 5 
                                #2 acdeg  1:1, 7:2,  4:2
                                #3 acdfg  1:2, 7:3,  4:3
                                #5 abdfg  1:1  7:2   4:3
                                
                                o1 = overlap(mapping[1],d)
                                o7 = overlap(mapping[7],d)
                                o4 = overlap(mapping[4],d)
                  
                                
                                if o1 ==1 and o7 == 2 and o4 == 2:
                                        digit = 2                                        
                                elif o1 ==2 and o7 == 3 and o4 == 3:
                                        digit = 3                                        
                                elif o1 ==1 and o7 == 2 and o4 == 3:
                                        digit = 5                                        
                        elif l == 6: # 0 6 9
                                #0 abcefg 1:2  7:3 4:3
                                #6 abdefg 1:1  7:2 4:3
                                #9 abcdfg 1:2  7:3 4:4
                
                                o1 = overlap(mapping[1],d)
                                o7 = overlap(mapping[7],d)
                                o4 = overlap(mapping[4],d)
                                if o1==2 and o7==3 and o4==3:
                                        digit=0
                                elif o1==1 and o7==2 and o4==3:
                                        digit=6
                                elif o1==2 and o7==3 and o4==4:
                                        digit=9                                        
                        elif l == 7:
                                digit = 8
                        else:
                                print("unknown length: {} {}".format(l,d))
                                print(line)
                                sys.exit()

                        if (digit == -1):
                                print("not complete")
                                sys.exit()

                        subsum = subsum + factor * digit
                        factor = factor / 10

                sum = sum + subsum
        return sum

filename = sys.argv[1]
print(doit(filename))


