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


results=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    length = int(sys.stdin.readline().rstrip())
    text = sys.stdin.readline().rstrip()
    justFound = 0
    for num in range(length - 5):
        if justFound > 0:
            justFound = justFound - 1
            continue
        rev = text[num + 2] + text[num + 1] + text[num]
        if rev in text:
            result = ""
            done = False
            i = num + 3
            apdR = True
            while not done:
                char = text[i]
                try:
                    nextChar = text[i + 1]
                    if rev == text[i] + nextChar + text[i+2]:
                        done = True
                        break
                except:
                    done = True
                    apdR = False
                    break
                if char == nextChar:
                    if char == rev[0] or char == rev[1] or char == rev[2]:
                        i += 1
                result = result + char
                i += 1
            if apdR:
                justFound = len(result) + 2
                results.append(result)

for r in results:
    print(r)



