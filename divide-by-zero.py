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

for nums in bank:
    dividend, divisor = nums.split()
    try:
        dividend = float(dividend)
        try:
            divisor = float(divisor)
            if not divisor == 0:
                output = dividend / divisor
                output = round(output + 1e-9, 1)
                output = str(output)
                print(output)
            else:
                print("Divide By Zero")
        except:
            print("Invalid Divisor")
    except:
        print("Invalid Dividend")



