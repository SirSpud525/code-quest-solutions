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

for eq in bank:
    nums = eq.split()
    output = f"{round(eval(nums[0] + nums[1] + nums[2]), 1):.1f}"
    output = output + " " + f"{round(eval(nums[2] + nums[1] + nums[0]) + 1e-9, 1):.1f}"
    print(output)



