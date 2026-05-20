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

result=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    items = int(sys.stdin.readline().rstrip())
    estimates = (sys.stdin.readline().rstrip()).split()
    actuals = (sys.stdin.readline().rstrip()).split()
    total = 0
    for i in range(items):
        estimates[i] = Decimal(estimates[i])
        actuals[i] = Decimal(actuals[i])
        diff = actuals[i] - estimates[i]
        total += diff
    average = total / items
    average = average.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    average = f"{average:.2f}"
    result.append(average)

for r in result:
    print(r)



