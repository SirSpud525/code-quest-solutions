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

sequence = [0, 1]

curLoco = 2

for i in range(1000):
    sequence.append(sequence[curLoco - 2] + sequence[curLoco - 1])
    curLoco += 1

for number in bank:
    if int(number) in sequence:
        print("TRUE")
    else:
        print("FALSE")



