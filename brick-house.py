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
    bank.append((sys.stdin.readline().rstrip()))

for bricks in bank:
    small, large, target = list(map(int, bricks.split()))
    if large >= math.floor(target/5):
        if small >= target % 5:
            print("true")
        else:
            print("false")
    else:
        if target - (large * 5) <= small:
            print("true")
        else:
            print("false")





