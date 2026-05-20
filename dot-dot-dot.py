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

alphabet = list("abcdefghijklmnopqrstuvwxyz")

bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for dot in bank:
    output = 0
    dot = list(dot)
    for c in dot:
        output += alphabet.index(c) + 1
    print(output)



