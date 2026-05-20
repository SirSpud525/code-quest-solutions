# Recommended imports for all problems
# Some problems may require more
#IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

getcontext().prec = 50

bank=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for nums in bank:
    aorg, borg = list(map(float, nums.split()))
    a = 0.0
    b = 0.0
    aold = 0.0
    z = 0
    i = 0
    while abs(z) < 100 and i < 55:
        aold = a
        a = (a * a) + aorg + - (b * b)
        b = (aold * b * 2) + borg
        z = math.sqrt(a * a + b * b)
        i += 1
    toOut = ""
    if i <= 10:
        toOut = "RED"
    elif i <= 20:
        toOut = "ORANGE"
    elif i <= 30:
        toOut = "YELLOW"
    elif i <= 40:
        toOut = "GREEN"
    elif i <= 50:
        toOut = "BLUE"
    else:
        toOut = "BLACK"
    print(nums.split()[0] + "+" + nums.split()[1] + "i " + toOut)
