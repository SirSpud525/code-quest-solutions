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

getcontext().prec = 100
results=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    c = [["", ""],["", ""]]
    f = ["", ""]
    c[0][0], c[1][0] = list(map(Decimal, sys.stdin.readline().rstrip().split()))
    c[0][1], c[1][1] = list(map(Decimal, sys.stdin.readline().rstrip().split()))
    f[0], f[1] = list(map(Decimal, sys.stdin.readline().rstrip().split()))
    inv = [["",""],["",""]]
    det = (c[0][0] * c[1][1]) - (c[1][0] * c[0][1])
    inv[0][0] = c[1][1] / det
    inv[0][1] = -1 * c[0][1] / det
    inv[1][0] = -1 * c[1][0] / det
    inv[1][1] = c[0][0] / det
    e = ["",""]
    e[0] = (inv[0][0] * f[0]) + (inv[0][1] * f[1])
    e[1] = (inv[1][0] * f[0]) + (inv[1][1] * f[1])
    e[0] = e[0].quantize(Decimal(1), ROUND_HALF_UP)
    e[1] = e[1].quantize(Decimal(1), ROUND_HALF_UP)
    results.append(" ".join(list(map(str, e))))


for r in results:
  print(r)