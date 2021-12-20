import re
import sys
import numpy as np

def add(line1,line2):
    return "[" + line1 + "," + line2 + "]"

def split(line):
    parts = re.split('([^0-9])',line)
    for i in range(len(parts) -1,-1,-1):
        if len(parts[i]) == 0:
            del parts[i]

#    print("".join(parts))
    for i in range(len(parts)):
        if parts[i].isdigit() and int(parts[i]) > 9:
            n = int(parts[i])
            del parts[i]
            parts.insert(i,']')
            parts.insert(i, str(n - n // 2 ))
            parts.insert(i,',')
            parts.insert(i, str(n // 2))
            parts.insert(i,'[')
 
            
#            print("".join(parts))
            
            return True, "".join(parts)

    return False, "".join(parts)


def explode(line):
#    print(line)
    parts = re.split('([^0-9])',line)
    for i in range(len(parts) -1,-1,-1):
        if len(parts[i]) == 0:
            del parts[i]
#    print("###########")
#    print("".join(parts))
    
    depth = 0
    for i in range(len(parts)):
        if parts[i] == '[':
            depth += 1
        elif parts[i] == ']':
            depth -= 1
        elif parts[i] == ',':
            pass
        elif parts[i].isdigit():
 #           print("number {} at depth {}".format(parts[i],depth))
            if depth == 5:                                    
 #               print("We should explode now")

                # i - 1 [
                # i     n1
                # i + 1 ,
                # i + 2 n2
                # i + 3 ]
                    
                # get the previous number
                j = i - 1
                prev = False
                while j > 0:
                    if parts[j].isdigit():
  #                      print("Previous number = {} at {}".format(parts[j],j))
                        parts[j] = str(int(parts[j]) + int(parts[i]))
                        prev = True
                        j = 0                    
                    j -= 1
                if prev == False:
                    parts[i] = '0'

                # get the previous number
                next = False
                j = i + 3
                while j < len(parts):
                    if parts[j].isdigit():
 #                       print("Next number = {} at {}".format(parts[j],j))
                        parts[j] = str(int(parts[j]) + int(parts[i+2]))                
                        j = len(parts)
                        next = True
                    j += 1

                if next == False:
                    parts[i+2] = '0'
                    
                #                del parts[i + 3]
                #del parts[i + 1]
                #del parts[i - 1]

                if prev == False and next == True:
                    del parts[i+3]
                    del parts[i+2]
                    del parts[i+1]
                    del parts[i-1]
                elif prev == True and next == False:
                    del parts[i+3]
                    del parts[i+1]
                    del parts[i]
                    del parts[i-1]
                elif prev == True and next == True:
                    parts[i-1] = '0'
                    del parts[i+3]
                    del parts[i+2]
                    del parts[i+1]
                    del parts[i]
                    
#                print("".join(parts))
                return True, "".join(parts)
    return False, "".join(parts)


def reduce(line):
#    print(line)
    cont = True
    while cont:
        cont = False

        # try explode first
        didexplode, line = explode(line)
        if didexplode == True:
#            print("Explode: {}".format(line))
            cont = True
        else:
            didsplit, line = split(line)
            if didsplit == True:
#                print("Split: {}".format(line))
                cont = True

    return line


def doit(filename):
    file = open(filename, 'r')

    number = None
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) < 2:
            break
        line = line.strip()

        if number is None:
            number = line
        else:
            number = add(number,line)
            number = reduce(number)
    return number

def magnitude(line):
    parts = re.split('([^0-9])',line)
    for i in range(len(parts) -1,-1,-1):
        if len(parts[i]) == 0:
            del parts[i]
#    print("".join(parts))

    cont = True
    while cont:
        cont = False

        i = 0
        while i < len(parts) - 4:
#            print(len(parts),i)
            if parts[i] == '[' and parts[i+1].isdigit() and parts[i+2] == ',' and parts[i+3].isdigit() and parts[i+4] == ']':
                parts[i] = str(3 * int(parts[i+1]) + 2 * int(parts[i+3]))
                del parts[i+1]
                del parts[i+1]
                del parts[i+1]
                del parts[i+1]
                cont = True
            i += 1
#        print("".join(parts))
    

    return int(parts[0])
            
assert(explode('[[[[[9,8],1],2],3],4]') == (True, '[[[[0,9],2],3],4]'))
assert(explode('[7,[6,[5,[4,[3,2]]]]]') == (True, '[7,[6,[5,[7,0]]]]'))
assert(explode('[[6,[5,[4,[3,2]]]],1]') == (True, '[[6,[5,[7,0]]],3]'))
assert(explode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]') == (True, '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'))
assert(explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]') == (True, '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'))
assert(split('[[[[0,7],4],[15,[0,13]]],[1,1]]') == (True, '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'))
assert(split('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]') == (True, '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'))
assert(add('[[[[4,3],4],4],[7,[[8,4],9]]]','[1,1]') == '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
assert(reduce('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]') == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
assert(doit('sample12.dat') == '[[[[5,0],[7,4]],[5,5]],[6,6]]')
assert(doit('sample13.dat') == '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
assert(magnitude('[[1,2],[[3,4],5]]') == 143)
assert(magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]') == 1384)
assert(doit('sample14.dat') == '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')
assert(magnitude('[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]') == 4140)

print(magnitude(doit('input.dat')))
