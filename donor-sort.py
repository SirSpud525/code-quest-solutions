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


def formatAndPrint(inputList):
    if len(inputList) == 0:
        print()
    else:
        output = inputList[0]
        inputList.pop(0)
        for donor in inputList:
            output = output + "," + donor
        print(output)


bank = []
# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases * 2):
    bank.append((sys.stdin.readline().rstrip()))

curInd = 0

for donors in range(cases):
    lastYear = bank[curInd].split(',')
    thisYear = bank[curInd + 1].split(',')

    lastOnly = []
    thisOnly = []
    both = []

    for donor in lastYear:
        if donor in thisYear:
            both.append(donor)
        else:
            lastOnly.append(donor)

    for donor in thisYear:
        if not donor in lastYear:
            thisOnly.append(donor)

    lastOnly.sort()
    both.sort()
    thisOnly.sort()

    formatAndPrint(lastOnly)
    formatAndPrint(both)
    formatAndPrint(thisOnly)

    curInd += 2








