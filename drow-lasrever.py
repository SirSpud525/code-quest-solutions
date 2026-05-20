# Recommended imports for all problems
# Some problems may require more
#IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

bank=[]
uppers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for line in bank:
    line = list(line)
    new = []
    length = 0
    for c in range(len(line)):
        if line[c] in uppers or line[c] in lowers:
            length += 1
        else:
            for i in range(length):
                new.append(line[c-i-1])
            new.append(line[c])
            length = 0
    for i in range(length):
        new.append(line[len(line) - i - 1])
    for c in range(len(line)):
        if line[c] in uppers:
            new[c] = new[c].upper()
        else:
            new[c] = new[c].lower()
    print("".join(new))

