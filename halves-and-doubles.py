# Recommended imports for all problems
# Some problems may require more
#IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import binascii

bank=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for nums in bank:
    num1, num2 = list(map(int, nums.split()))
    result = 0
    print1 = str(num1) + " " + str(num2)
    if num1 % 2 == 0:
            print1 = print1 + " ***"
    else:
        result += num2
    print(print1)
    while num1 > 1:
        temp = num1
        num1 = int(num1/2)
        num2 = num2*2
        toPrint = str(num1)
        if not (Decimal(temp) / 2) == num1:
            toPrint = toPrint + "*"
        toPrint = toPrint + " " + str(num2)
        if num1 % 2 == 0:
            toPrint = toPrint + " ***"
        else:
            result += num2
        print(toPrint)
    print(result)

