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
# strinp out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))
    bank.append((sys.stdin.readline().rstrip()))
    bank.append((sys.stdin.readline().rstrip()))

i = 0

for case in range(int(len(bank) / 3)):

    n = int(bank[i])

    if n == 0:
        print("0.00")
    else:
        estimates = bank[i + 1].split()
        actuals = bank[i + 2].split()

        varianceTotal = 0

        for item in range(n):
            varianceTotal += (float(actuals[item]) - float(estimates[item]))

        result = varianceTotal / n
        result = round(result + 1e-9, 2)
        result = (f"{result:.2f}")

        print(result)

    i += 3

