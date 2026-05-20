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
import operator


results=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    newCases = int(sys.stdin.readline().rstrip())
    text = sys.stdin.readline().rstrip()
    for key in range(newCases):
        key = sys.stdin.readline().rstrip()
        c = 0
        result = "["
        for i in range(64):
            textValue = bin(int(text[c] + text[c+1], 16))[2:]
            keyValue = bin(int(key[c] + key[c+1], 16))[2:]
            textValue = f"{textValue:0>8}"
            keyValue = f"{keyValue:0>8}"
            toAdd = ""
            for j in range(8):
                if textValue[j] == keyValue[j]:
                    toAdd = toAdd + "0"
                else:
                    toAdd = toAdd + "1"
            toAdd = chr(int(toAdd,2))
            result = result + toAdd
            c+=2
        result = result + "]"
        results.append(result)


for r in results:
    print(r)


