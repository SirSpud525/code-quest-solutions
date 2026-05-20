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
# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for direction in bank:
    dirs = list(direction)
    x = 0
    y = 0
    for dir in dirs:
        if dir == "L":
            x -= 1
        elif dir == "R":
            x += 1
        elif dir == "U":
            y += 1
        else:
            y -= 1

    if x == 0 and y == 0:
        print("TRUE")
    else:
        print("FALSE")

