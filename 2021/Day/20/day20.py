import re
import sys
import numpy as np

def getpixel(r,c,image,algorithm,background):
    pixels = ""
    for d in [[r-1,c-1],[r-1,c],[r-1,c+1],[r,c-1],[r,c],[r,c+1],[r+1,c-1],[r+1,c],[r+1,c+1]]:
        if 0 <= d[0] < len(image) and 0 <= d[1] < len(image[0]):
            pixels += image[d[0]][d[1]]
        else:
            pixels += background
    return algorithm[int(pixels.replace('.','0').replace('#','1'),2)]

def load(filename):
    file = open(filename, 'r')    

    algorithm = file.readline().strip()
    print(len(algorithm))
    file.readline()

    image = []
    while True:
        line = file.readline()
        if not line:
            break
        image.append(line.strip())

    print("image")
    return image,algorithm


def enhance(image,algorithm,background):
    newimage = []
    for r in range(-1,len(image)+1):
        row = ""
        for c in range(-1,len(image[0])+1):
            row += getpixel(r,c,image,algorithm,background)
        newimage.append(row)    
    return newimage

def part1(image,algorithm):
    background = '.'
    for step in range(2):
        image = enhance(image,algorithm,background)

        bgpixels = background * 9        
        background = algorithm[int(bgpixels.replace('#','1').replace('.','0'),2)]
        
    n = 0
    for row in image:
        n += row.count('#')
    return n

def part2(image,algorithm):
    background = '.'
    for step in range(50):
        image = enhance(image,algorithm,background)

        bgpixels = background * 9        
        background = algorithm[int(bgpixels.replace('#','1').replace('.','0'),2)]
        
    n = 0
    for row in image:
        n += row.count('#')
    return n


image,algorithm = load('sample.dat')
print("\n".join(image))
assert(len(algorithm)==512)
assert(getpixel(2,2,image,algorithm,'.') == '#')
assert(part1(image,algorithm) == 35)
assert(part2(image,algorithm) == 3351)

image,algorithm = load('input.dat')
print("Solution of part 1 = {}".format(part1(image,algorithm)))
print("Solution of part 2 = {}".format(part2(image,algorithm)))






