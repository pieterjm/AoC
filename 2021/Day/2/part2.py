import re
import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

depth = 0
position = 0
aim = 0
 
alen = len(lines)

for line in lines:
	m = re.search('^(forward|up|down) (\d+)', line)
	command = m.group(1)
	steps = int(m.group(2))
	if command == 'forward':
		position = position + steps
		depth = depth + aim * steps
	elif command == 'up':
		aim = aim - steps
	elif command == 'down':
		aim = aim + steps
	else:
		print("unknown command!!!")		
#	print("command = {}, steps = {}, depth = {}, position = {}".format(command,steps,depth,position))
print(depth * position)

