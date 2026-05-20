# Recommended imports for all problems
# Some problems may require more
#IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
import binascii

#initialize empty list m(rows) by n(columns)
def makelist(m,n,filler):
    a = [filler for x in range(m)]
    b = [[filler] * n for i in range(m)]
    return b

results = []
bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    info = str((sys.stdin.readline().rstrip())).split()
    info = list(map(int, info))
    grid = makelist(info[0], info[1], "")
    for bomb in range(info[2]):
        coords = str((sys.stdin.readline().rstrip())).split()
        coords = list(map(int, coords))
        grid[coords[0]][coords[1]] = "*"
    for rowNum in range(info[0]):
        for colNum in range(info[1]):
            mines = 0
            checkRow = -1
            while checkRow < 2:
                checkCol = -1
                while checkCol < 2:
                    if rowNum + checkRow >= 0 and colNum + checkCol >= 0 and rowNum + checkRow < info[0] and colNum + checkCol < info[1]:
                        if grid[rowNum + checkRow][colNum + checkCol] == "*":
                            mines += 1
                    checkCol += 1
                checkRow += 1
            if not grid[rowNum][colNum] == "*":
                grid[rowNum][colNum] = str(mines)
    for row in grid:
        result = ""
        for col in row:
            result = result + str(col)
        results.append(result)

for thing in results:
    print(thing)