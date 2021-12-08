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

while file.readline():
        bingocard = []
        for r in range(5):
                row = file.readline().split()
                for c in range(5):
                        row[c] = int(row[c])
                bingocard.append(row)
        #print(bingocard)
        cards.append(bingocard)


def sumunmarked(card):
        sum = 0
        for r in range(5):
                for c in range(5):
                        if card[r][c] > 0:
                                sum = sum + card[r][c]
        return sum


for number in numbers:

        # mark the number in all the cards
        for b in range(len(cards)):        
                for r in range(5):
                        for c in range(5):
                              if cards[b][r][c] == number:
                                      cards[b][r][c] = -1 * number
        
        # check bingo
        for b in range(len(cards)):

                # rows
                for r in range(5):
                        bingo = True
                        for c in range(5):
                                if cards[b][r][c] > 0:
                                        bingo = False
                        if bingo:
                                print(sumunmarked(cards[b])*number)
                                sys.exit()
                # cols
                for c in range(5):
                        bingo = True
                        for r in range(5):
                                if cards[b][r][c] > 0:
                                        bingo = False
                        if bingo:
                                print(sumunmarked(cards[b])*number)
                                sys.exit()
                                
                                





        

