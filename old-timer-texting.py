# Recommended imports for all problems
# Some problems may require more
# IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import binascii

bank = []
keys = [[" "], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"],
        ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]

# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for text in bank:
    result = ""
    for c in text:
        for i in keys:
            for j in i:
                if j == c:
                    for k in range(i.index(j) + 1):
                        result = result + str(keys.index(i))
                    result = result + "-"
    result = result[:-1]
    print(result)