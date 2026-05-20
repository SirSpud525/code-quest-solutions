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
    height, length = sys.stdin.readline().rstrip().split()
    initial = []
    for i in range(int(height)):
        initial.append(sys.stdin.readline().rstrip().split(','))
    new = []
    for i in range(int(length)):
        row = []
        for j in range(int(height)):
            row.append(initial[j][i])
        new.append(row)
    for i in range(int(length)):
        res = ",".join(new[i])
        results.append(res)

for r in results:
    print(r)
