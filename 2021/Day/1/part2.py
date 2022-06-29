import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

prev = -1
count = 0
 
alen = len(lines)


for i in range(1,alen-2,1):
	prev = int(lines[i-1]) + int(lines[i]) + int(lines[i+1])
	depth = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])	
	if depth > prev:
		count = count + 1
	print("prev = {}, depth = {}, count = {}".format(prev,depth,count))
		
print(count)
