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

def listFactors(num):
    factor = num
    result = []
    # result.append(1)
    result.append(num)
    while factor > 1:
        factor -= 1
        trying = 2
        while factor >= trying:
            if trying * factor == num:
                result.append(factor)
                if factor != trying:
                    result.append(trying)
            trying += 1
    result.sort()
    return result

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for text in bank:
  dists = []
  c = 0
  end = len(text) - 2
  while c < end:
    bit = text[c:c+2]
    i = c + 3
    while i < end:
      if bit == text[i:i+2]:
        j = 2
        while text[c:c+j] == text[i:i+j]:
          j += 1
        j -= 1
        dists.append(i-c)
        # print(i,c,j,text[c:c+j],text[i:i+j])
        c += j - 1
        break
      i += 1
    c += 1
  factors = []
  for i in dists:
    for f in listFactors(i):
      factors.append(f)
  d = Counter(factors)
  common = d.most_common(3)
  k = 0
  while common[k][0] == 2 or common[k][0] == 3:
    k += 1
  print(common[k][0])
