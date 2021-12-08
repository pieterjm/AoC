import sys
import os
import subprocess
import re

year = sys.argv[1]
day  = sys.argv[2]

basedir = os.path.join(year,'Day',day)

inputdat = os.path.join(basedir,'input.dat')
sampledat = os.path.join(basedir,'sample.dat')
part1 = os.path.join(basedir,'part1.py')
part2 = os.path.join(basedir,'part2.py')

if os.path.isfile(part1):
	if os.path.isfile(sampledat):
		print("Solution part1 for sample data on day {} of {}".format(day,year))
		subprocess.call(['python',part1,sampledat])
	if os.path.isfile(inputdat):
		print("Solution part1 for input data on day {} of {}".format(day,year))
		subprocess.call(['python',part1,inputdat])
else:
	print("No part1 solution for day {} of {} yet".format(day,year))

if os.path.isfile(part2):
	if os.path.isfile(sampledat):
		print("Solution part2 for sample data on day {} of {}".format(day,year))
		subprocess.call(['python',part2,sampledat])
	if os.path.isfile(inputdat):
		print("Solution part2 for input data on day {} of {}".format(day,year))
		subprocess.call(['python',part2,inputdat])
else:
	print("no part2 solution for day {} of {} yet".format(day,year))
