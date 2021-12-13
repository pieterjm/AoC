import re
import sys
import numpy as np

i = 0

def parse(l):
    global i
    print("Start parsing at i={} ".format(i))
    
    node = {
        'nchilds': int(l[i]),
        'nmeta': int(l[i+1]),
        'meta': [],
        'childs': []
    }
    i += 2
    
    for n in range(node['nchilds']):
        print("Start parsing child at i={}".format(i))
        child = parse(l)
        node['childs'].append(child)
        print("Finished parsing child at {}".format(i))
        
    print("starting to read metadata at {}".format(i))
    for n in range(node['nmeta']):
        node['meta'].append(int(l[i+n]))
    i += node['nmeta']
        
    return node

def getvalue(node):
    print("Get value")
    if node['nchilds'] == 0:
        return sum(node['meta'])
    else:
        s = 0
        for id in node['meta']:            
            print("meta {} child {}".format(id - 1,node['nchilds']))
            id = id - 1
            if 0 <= id < node['nchilds']:
                s += getvalue(node['childs'][id])

        return s

def summeta(node):
    s = sum(node['meta'])
    for child in node['childs']:
        s += summeta(child)
    return s
    
def doit(filename):
    file = open(filename, 'r')
    line = file.readline().split(' ')


    global i
    i = 0
    tree = parse(line)
    print(tree)

    return getvalue(tree)


filename = sys.argv[1]
print(doit(filename))


