import re
from array import *
import sys

file = open(sys.argv[1], 'r')

line = file.readline()
numbers = line.split(',')
#print(numbers)

for i in range(len(numbers)):
        numbers[i] = int(numbers[i])


cards = []
won = []

while file.readline():
        bingocard = []
        for r in range(5):
                row = file.readline().split()
                for c in range(5):
                        row[c] = int(row[c])
                bingocard.append(row)
        #print(bingocard)
        cards.append(bingocard)
        won.append(False)

def sumunmarked(card):
        sum = 0
        for r in range(5):
                for c in range(5):
                        if card[r][c] > 0:
                                sum = sum + card[r][c]
        return sum

solution = -1
for number in numbers:
        # mark the number in all the cards
        for b in range(len(cards)):
                if won[b] == False:
                        for r in range(5):
                                for c in range(5):
                                        if cards[b][r][c] == number:
                                                cards[b][r][c] = -1
        
        # check bingo
        for b in range(len(cards)):
                if won[b] == False:
                        # rows
                        for r in range(5):
                                bingo = True
                                for c in range(5):
                                        if cards[b][r][c] != -1:
                                                bingo = False
                                if bingo:
					solution = sumunmarked(cards[b])*number
                                        #print("Card {} wins with score {}".format(b,sumunmarked(cards[b])*number))
                                        won[b] = True

                # cols
                if won[b] == False:
                        for c in range(5):
                                bingo = True
                                for r in range(5):
                                        if cards[b][r][c] != -1:
                                                bingo = False
                                if bingo:
					solution = sumunmarked(cards[b])*number
                                        #print("Card {} wins with score {}".format(b,sumunmarked(cards[b])*number))
                                        won[b] = True                                
                                


print(solution)



        

