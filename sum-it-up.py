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
    num1, num2 = nums.split()
    num1 = int(num1)
    num2 = int(num2)
    if num1 == num2:
        print(2 * (num1 + num2))
    else:
        print(num1 + num2)
