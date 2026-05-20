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

for info in bank:
    part1, part2 = info.split()
    if part1 == "true":
        part1 = True
    else:
        part1 = False
    if part2 == "true":
        part2 = True
    else:
        part2 = False
    if (part1 and part2) or (not part1 and not part2):
        print("true")
    else:
        print("false")