import re
import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

depth = 0
position = 0
aim = 0
 
alen = len('010100101101')

numone = [0,0,0,0,0,0,0,0,0,0,0,0]
numnul = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in lines:
	for i in range(12):
		if (line[i] == '1'):
			numone[i] = numone[i] + 1
		elif (line[i] == '0'):
			numnul[i] = numnul[i] + 1
		else:
			print("ilegal character")
			print(line)

gamma = ''
epsilon = ''
for i in range(12):
	if numone[i] > numnul[i]:
		gamma += '1'
		epsilon += '0'
	elif numone[i] < numnul[i]:
		gamma += '0'
		epsilon += '1'
	else:
		print("numbers are equal")

print(int(gamma,2) * int(epsilon,2))

