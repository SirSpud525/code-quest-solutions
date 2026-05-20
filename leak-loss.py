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

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
  bank.append(sys.stdin.readline().rstrip())

for nums in bank:
  volume, fill, leak = list(map(float, nums.split()))
  output =  volume * leak / (fill - leak)
  output = int(round(output + 1e-9, 0))
  print(output)
