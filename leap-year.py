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

bank=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    newCase = int((sys.stdin.readline().rstrip()))
    for thing in range(newCase):
        bank.append((sys.stdin.readline().rstrip()))

for year in bank:
    year = int(year)
    if year < 1582:
        print("No")
    elif year % 4 != 0:
        print("No")
    elif year % 100 != 0:
        print("Yes")
    elif year % 400 != 0:
        print("No")
    else:
        print("Yes")

