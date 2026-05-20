# Recommended imports for all problems
# Some problems may require more
# IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
import binascii

bank = []
# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for item in bank:
    times, herald = item.split()
    if int(times) > int(herald):
        diff = int(times) - int(herald)
        print("Times has " + str(diff) + " more subscribers")
    elif int(herald) > int(times):
        diff = int(herald) - int(times)
        print("Herald has " + str(diff) + " more subscribers")
    else:
        print("Times and Herald have the same number of subscribers")

