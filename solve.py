import sys
import os
import subprocess
import re

year = None
day = None


if len(sys.argv) == 2:
	year = sys.argv[1]
elif len(sys.argv) == 3:
	year = sys.argv[1]
	day = sys.argv[2]
else:
	print("Call this scripts with one or two argumenrs: the year and optionally a day.")
	sys.exit()

if not re.search("^\d{4}$",year):
	print("The year format is not correct. Use four digits")
	sys.exit()
if day is not None and not re.search("^[1-9][0-9]?$",day):
	print("The day format is not correct, use the number of the day without a zero as prefix.")
	sys.exit()


days = []
if day is not None:
	day = int(day)
	days = range(day,day + 1)
else:
	days = range(1,26)

for day in days:
	print("#########################################")
	print("##### Solution for day {} of {}".format(day,year))
	basedir = os.path.join(year,'Day',str(day))

	inputdat = os.path.join(basedir,'input.dat')
	sampledat = os.path.join(basedir,'sample.dat')
	part1 = os.path.join(basedir,'part1.py')
	part2 = os.path.join(basedir,'part2.py')

	if os.path.isfile(part1):
		if os.path.isfile(sampledat):
			print("## Solution part1 for sample data on day {} of {}".format(day,year))
			subprocess.call(['python',part1,sampledat])
		if os.path.isfile(inputdat):
			print("## Solution part1 for input data on day {} of {}".format(day,year))
			subprocess.call(['python',part1,inputdat])
	else:
		print("No part1 solution for day {} of {} yet".format(day,year))

	if os.path.isfile(part2):
		if os.path.isfile(sampledat):
			print("## Solution part2 for sample data on day {} of {}".format(day,year))
			subprocess.call(['python',part2,sampledat])
		if os.path.isfile(inputdat):
			print("## Solution part2 for input data on day {} of {}".format(day,year))
			subprocess.call(['python',part2,inputdat])
	else:
		print("no part2 solution for day {} of {} yet".format(day,year))
