# Recommended imports for all problems
# Some problems may require more
# IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
import binascii

bank = []
output = []
# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases * 3):
    bank.append((sys.stdin.readline().rstrip()))

i = 0

for move in range(cases):
    boardX, boardY = bank[i].split(",")
    i += 1
    startX, startY = bank[i].split(",")
    i += 1
    endX, endY = bank[i].split(",")
    i += 1

    boardX = int(boardX)
    boardY = int(boardY)
    startX = int(startX)
    startY = int(startY)
    endX = int(endX)
    endY = int(endY)

    if startX % 2 == startY % 2:
        startColor = 0
    else:
        startColor = 1

    if endX % 2 == endY % 2:
        endColor = 0
    else:
        endColor = 1

    if startColor == endColor:
        if endX <= boardX and endY <= boardY:
            print("Yes")
        else:
            print("No")
    else:
        print("No")





