import re
import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

depth = 0
position = 0
 
alen = len(lines)

for line in lines:
	m = re.search('^(forward|up|down) (\d+)', line)
	command = m.group(1)
	steps = int(m.group(2))
	if command == 'forward':
		position = position + steps
	elif command == 'up':
		depth = depth - steps
	elif command == 'down':
		depth = depth + steps
	else:
		print("unknown command!!!")		
print(depth * position)

