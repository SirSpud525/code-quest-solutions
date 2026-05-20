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
  newCases = int(sys.stdin.readline().rstrip())
  values = []
  for that in range(newCases):
    values.append(sys.stdin.readline().rstrip())
  values = list(map(Decimal, values))
  mm = sorted(values)
  max = mm[len(mm) - 1]
  min = mm[0]
  divisor = max - min
  for value in values:
    output = (value - min) / (divisor)
    output = output * Decimal("255")
    output = output.quantize(Decimal(1), ROUND_HALF_UP)
    results.append(output)



for r in results:
  print(r)