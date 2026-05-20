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
    gens = int(sys.stdin.readline().rstrip())
    old = []
    new = []
    for i in range(10):
      new.append([])
    for i in range(10):
      old.append(list(sys.stdin.readline().rstrip()))
    for e in range(gens):
        for i in range(10):
            for j in range(10):
              s = 0
              for k in [-1,0,1]:
                  for h in [-1,0,1]:
                      if i+k >= 0 and j+h >= 0 and i+k < 10 and j+h < 10:
                          if not (k == 0 and h == 0):
                            s += int(old[i+k][j+h])
              if s <= 1:
                  new[i].append("0")
              elif s == 3:
                  new[i].append("1")
              elif s >= 4:
                  new[i].append("0")
              else:
                  new[i].append(old[i][j])
        old = new.copy()
        new = []
        for f in range(10):
            new.append([])
    for i in range(10):
        results.append("".join(old[i]))


for r in results:
  print(r)