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

result=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    items = int(sys.stdin.readline().rstrip())
    estimates = (sys.stdin.readline().rstrip()).split()
    actuals = (sys.stdin.readline().rstrip()).split()
    total = 0
    for i in range(items):
        estimates[i] = float(estimates[i])
        actuals[i] = float(actuals[i])
        diff = actuals[i] - estimates[i]
        total += diff
    average = total / items
    average = round(average + 1e-9, 2)
    average = f"{average:.2f}"
    result.append(average)

for r in result:
    print(r)




