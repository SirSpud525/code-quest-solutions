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

alphabet = list("0ABCDEFGHIJKLMNOPQRSTUVWXYZ")
bank = []

# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for case in bank:
    case = list(case)
    result = ""
    for thing in case:
        dig = thing
        temp = dig
        dig = alphabet.index(dig)
        if dig >= 21:
            done = False
            factor = dig
            while not done:
                factor -= 1
                trying = 2
                if factor == 1:
                    done = True
                while trying <= factor and not done:
                    if factor * trying == dig:
                        done = True
                    trying += 1
            dig = factor * 2
        elif dig >= 16:
            dig = str(dig)
            dig = (int(dig[0]) + int(dig[1])) * 8
        elif dig >= 11:
            dig = ((dig % 3) * 5) + 1
        elif dig >= 6:
            dig = dig * dig
        else:
            dig = dig + 6

        while dig > 26:
            dig = dig - 26

        if dig == 0:
            dig = temp
        else:
            dig = alphabet[dig]
        result = result + dig
    print(result)

