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

for input in bank:
    newInput = input.split(' ')
    result = (int(newInput[0]) * 2) + ((int(newInput[1]) + int(newInput[2])) * 4)
    print(result)
