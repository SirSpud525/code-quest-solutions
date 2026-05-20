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

for nums in bank:
    numG, numS = list(map(int, nums.split(",")))
    if numS > numG:
        temp = numS
        numS = numG
        numG = temp
    result = 1
    while result > 0:
        result = numG - numS
        print(str(numG) + "-" + str(numS) + "=" + str(result))
        if result > numS:
            numG = result
        else:
            numG = numS
            numS = result
    if numG == 1:
        print("COPRIME")
    else:
        print("NOT COPRIME")


