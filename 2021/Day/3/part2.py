import re
import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()
mlines = list(lines)
clines = list(lines)

depth = 0
position = 0
aim = 0
 
alen = 12

i = 0
while i < 12:
	# oxygen generator rating
	numone = 0
	numnul = 0
	if len(mlines) > 1:
		for line in mlines:
			# determine the most at position i
			if (line[i] == '1'):
				numone = numone + 1
			if (line[i] == '0'):
				numnul = numnul + 1

		if numone > numnul:
			mco = '1'
		elif numone < numnul:
			mco = '0'
		else:
			mco = '1'

		for line in list(mlines):
			if line[i] != mco:
				mlines.remove(line)

	# oxygen generator rating
	numone = 0
	numnul = 0
	if len(clines) > 1:
		for line in clines:
			# determine the most at position i
			if (line[i] == '1'):
				numone = numone + 1
			if (line[i] == '0'):
				numnul = numnul + 1

		if numone > numnul:
			cco = '0'
		elif numone < numnul:
			cco = '1'
		else:
			cco = '0'

		for line in list(clines):
			if line[i] != cco:
				clines.remove(line)

	i = i + 1


print(int(mlines[0],2) * int(clines[0],2))

