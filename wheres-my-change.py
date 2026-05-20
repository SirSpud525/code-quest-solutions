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
amounts = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.1, 0.05, 0.01]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for money in bank:
    money = int(round(float(money) * 100))
    result = ""
    i = 0
    while money >= 1:
        curNum = 0
        curMoney = int(amounts[i] * 100)
        while money >= curMoney:
            money -= curMoney
            curNum += 1
        result = result + str(curNum)
        i += 1
    result = f"{result:0<11}"
    print(result)
