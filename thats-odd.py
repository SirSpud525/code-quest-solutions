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

for num in bank:
    num = int(num)
    if num == 0:
        print("EVEN")
    elif num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

