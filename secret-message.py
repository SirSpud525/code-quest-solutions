# Recommended imports for all problems
# Some problems may require more
#IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import binascii

results=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    result = ""
    message = []
    for i in range(int(sys.stdin.readline().rstrip())):
        message.append(sys.stdin.readline().rstrip())
    y, x = list(map(int, sys.stdin.readline().rstrip().split(",")))
    lines = []
    for i in range(int(sys.stdin.readline().rstrip())):
        lines.append(sys.stdin.readline().rstrip())
    for line in lines:
        curX = x
        for c in line:
            if c == "O":
                result = result + message[y][curX]
            curX += 1
        y += 1
    results.append(result)

for r in results:
    print(r)


