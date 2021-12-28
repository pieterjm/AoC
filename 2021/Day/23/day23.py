import re
import sys
import numpy as np
import copy

state = {}

def load(filename):
    file = open(filename, 'r')    

    maze = []
    while True:
        line = file.readline()
        if not line:
            break
        line.strip()
        maze.append(list(line))
        
    return maze

def getkey(maze):
    key = ""
    for r in maze:
        key += "".join(r)
    return key

def step(maze):

    
    global state

    key = getkey(maze)
    if not key in state:
        print("Houston we got a problem")
        sys.exit(0)
        
#    print(key)
        
    # check if the solution of the maze is correct, if do all possible steps
    bSolved = True
    for a,r,c in [['A',2,3],['A',3,3],['B',2,5],['B',3,5],['C',2,7],['C',3,7],['D',2,9],['D',3,9]]:
        if maze[r][c] != a:
            bSolved = False
    if bSolved == True:
        print("Solved the maze")
        return

    # Create a list of all amphoids that can move somewhere
    m = []

    # check movements in the top row
    toprow = [1,2,4,6,8,10,11]
    for i in range(len(toprow)):
        c = toprow[i]
        if maze[1][c] != '.':
            if i > 0 and maze[1][toprow[i-1]] == '.':
                m.append([[1,c],[1,toprow[i-1]]])
            if i < (len(toprow) - 1) and maze[1][toprow[i+1]] == '.':
                m.append([[1,c],[1,toprow[i+1]]])

    # check movements in and out each cave
    caves = [['A',3],['B',5],['C',7],['D',9]]
    for a,c in caves:
        # check if we can move out of the cave at all
        to = []
        if maze[1][c-1] == '.':
            to.append([1,c-1])
        if maze[1][c+1] == '.':
            to.append([1,c+1])

        # if we can move out of the cave
        if len(to) > 0:
            if maze[2][c] != '.' and (maze[2][c] != a or maze[3][c] != a):
                for t in to:
                    m.append([[2,c],t])
            if maze[2][c] == '.' and maze[3][c] != a:
                for t in to:
                    m.append([[3,c],t])

        # move into the cave
        for t in [c-1,c+1]:
            if maze[1][t] == a:
                if maze[3][c] == '.' and maze[2][c] == '.':
                    m.append([[1,t],[3,c]])
                if maze[3][c] == a and maze[2][c] == '.':
                    m.append([[1,t],[2,c]])



            
    for s in m:
        steps = abs(s[1][0] - s[0][0]) + abs(s[1][1] - s[0][1])
        estep = 0
        if maze[s[0][0]][s[0][1]] == 'A':
            estep = steps * 1
        if maze[s[0][0]][s[0][1]] == 'B':
            estep = steps * 10
        if maze[s[0][0]][s[0][1]] == 'C':
            estep = steps * 100
        if maze[s[0][0]][s[0][1]] == 'D':
            estep = steps * 1000


        newmaze = copy.deepcopy(maze)        
        temp = newmaze[s[0][0]][s[0][1]]
        newmaze[s[0][0]][s[0][1]] = newmaze[s[1][0]][s[1][1]]
        newmaze[s[1][0]][s[1][1]] = temp

        
        
        newkey = getkey(newmaze)
        if not newkey in state:
            state[newkey] = {key:estep}
            step(newmaze)
        elif not key in state[newkey]:
            state[newkey][key] = estep

maze = load('input.dat')

state[getkey(maze)] = {}

step(maze)



print(len(state))

startkey = getkey(maze)
solutkey = '#############\n#...........#\n###A#B#C#D###\n  #A#B#C#D#\n  #########'

solution = {}
while True:
    count = 0
    for k1 in state:
        if k1 in solution:
            count += 1
        
        for k2 in list(state[k1]):
            if k2 == startkey:
                if not k1 in solution:
                    solution[k1] = state[k1][k2]
                elif state[k1][k2] < solution[k1]:
                    solution[k1] = state[k1][k2]                
            elif k2 in solution:
                if not k1 in solution:
                    solution[k1] = state[k1][k2] + solution[k2]
                elif state[k1][k2] + solution[k2] < solution[k1]:
                    solution[k1] = state[k1][k2] + solution[k2]
                    
    # print results            
    if solutkey in solution:
        print(solution[solutkey])
    else:
        print("no solution yet ",count)
