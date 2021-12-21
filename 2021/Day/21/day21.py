import re
import sys
import numpy as np

def load(filename):
    file = open(filename, 'r')    
    pos = []
    
    for p in range(2):
        line = file.readline().strip()

        m = re.search("^Player (\d+) starting position: (\d+)$",line)
        if m:
            pos.append(int(m.group(2)))

    return pos


def part1(pos):
    nplayers = 2
    score = []
    for p in range(nplayers):
        score.append(0)
    
    dice = 1
    current = 0
    nrolls = 0
    
    while True:
        # throw dice
        td = 0
        for _ in range(3):
            td += dice
            dice = (dice % 100) +1
            nrolls += 1
            
        # go to current position
        pos[current] = ((pos[current] - 1 + td) % 10) + 1
        
        score[current] += pos[current]

        #print("player {} moves to {} with dice {} and score {}".format(current + 1,pos[current],td,score[current]))
        
        if score[current] >= 1000:
            return score[1 - current] * nrolls
        

        # next player
        current = (current + 1 ) % nplayers


def part2(pin):
    p1 = pin[0]
    p2 = pin[1]
    
    # calculate the possible options and their frequencies after three rolls
    dfreq = {}
    for d1 in range(1,4):
        for d2 in range(1,4):
            for d3 in range(1,4):
                sd = d1 + d2 + d3
                if sd in dfreq:
                    dfreq[sd] += 1
                else:
                    dfreq[sd] = 1
    wins = [0,0]

    # game state hash
    gs = {}

    
    # set the initial game in  the state
    gs[repr([p1,p2,0,0])] = {'pos':[p1,p2],'score':[0,0],'weight':1}

    p = 0
    step = 0
    while True:
        # count number of games
        ngames = 0
        for k in gs:
            ngames += gs[k]['weight']
        if ngames == 0:
            print(wins)
            return max(wins)
    
        print("Step: {} ngames = {}".format(step,ngames))
        step += 1
        
        # copy state to new state and count number of games
        ngs = {}

        # iterate over games and play for player one and two
        for g in gs.values():
            # spawn new positions
            for td in dfreq:
                position = [g['pos'][0],g['pos'][1]]
                position[p] = ((position[p] - 1 + td ) % 10) + 1

                score = [g['score'][0],g['score'][1]]
                score[p] = score[p] + position[p]

                weight = g['weight'] * dfreq[td]
                
                if score[p] >= 21:                            
                    wins[p] += weight
                else:                        
                    # store this state
                    key = repr([position[0],position[1],score[0],score[1]])
                    if key in ngs:
                        ngs[key]['weight'] += weight
                    else:
                        ngs[key] = {'pos':[position[0],position[1]],'score':[score[0],score[1]],'weight':weight}
                    
        gs.clear()
        for k in ngs:
            gs[k] = {'pos':[ngs[k]['pos'][0],ngs[k]['pos'][1]],'score':[ngs[k]['score'][0],ngs[k]['score'][1]],'weight':ngs[k]['weight']}
                        
        p = 1 - p
        

                
assert(part1([4,8]) == 739785)
assert(part2([4,8]) == 444356092776315)

pos = load('input.dat')
print("Solution for part 1 = {}".format(part1(pos)))
pos = load('input.dat')
print("Solution for part 2 = {}".format(part2(pos)))







