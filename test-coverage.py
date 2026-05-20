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
    items = int(sys.stdin.readline().rstrip())
    toTest = (sys.stdin.readline().rstrip()).split(",")
    for i in range(items):
        line = (sys.stdin.readline().rstrip())
        line = line.split(",")
        for item in line:
            while item in toTest:
                toTest.remove(item)
    if len(toTest) != 0:
        results.append(",".join(sorted(toTest)))
    else:
        results.append("FULL COVERAGE")

for r in results:
    print(r)
