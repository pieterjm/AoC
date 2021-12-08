import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

prev = -1
count = 0
for i in ( lines ):
	depth = int(i)
	if ((prev!=-1)and(depth>prev)):
		count = count + 1
#	print("depth = {}, pdetph = {}, count = {}".format(depth,prev,count))
	prev = depth
	
print(count)
