# Recommended imports for all problems
# Some problems may require more
# IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

results = []
stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    classNum, charNum = list(map(int, sys.stdin.readline().rstrip().split()))
    classes = {}
    for c in range(classNum):
        dex, *order = (sys.stdin.readline().rstrip()).split()
        classes[dex] = order
    for c in range(charNum):
        myClass, *nums = (sys.stdin.readline().rstrip()).split()
        nums = sorted(list(map(int, nums)))
        output = {}
        for i in range(6):
            output[classes[myClass][i]] = nums[5 - i]
        results.append(myClass)
        for stat in stats:
            results.append(stat + ": " + str(output[stat]))

for r in results:
    print(r)