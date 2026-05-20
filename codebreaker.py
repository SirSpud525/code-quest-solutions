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

bank=[]
results = []
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    newCases = int(sys.stdin.readline().rstrip())
    lines = []
    for thing in range(newCases):
      lines.append(sys.stdin.readline().rstrip().upper())
    lines = "".join(lines)
    freqs = Counter(lines)
    keys = list(freqs.keys())
    for key in keys:
      if not key in alphabet:
        del freqs[key]
    keys = list(freqs.keys())
    total = Decimal(0)
    for key in keys:
      total += Decimal(freqs[key])
    for key in alphabet:
      pct = Decimal(freqs[key])/total * Decimal(100)
      pct = pct.quantize(Decimal("0.01"), ROUND_HALF_UP)
      results.append(str(key) + ": " + str(pct) + "%")

for r in results:
  print(r)