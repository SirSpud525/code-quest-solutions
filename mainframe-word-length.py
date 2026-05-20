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

results=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bits = int(sys.stdin.readline().rstrip())
    mx = pow(2,bits) - 1
    values = list(map(int, sys.stdin.readline().rstrip().split()))
    result = "TRUE"
    for v in values:
      if v > mx:
        result = "FALSE"
    results.append(" ".join([str(mx),result]))


for r in results:
  print(r)