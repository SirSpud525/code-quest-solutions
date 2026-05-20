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


results=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    width, height = list(map(int, sys.stdin.readline().rstrip().split()))
    text = sys.stdin.readline().rstrip()
    if len(text) > width:
        output = []
        good = True
        i = height
        while i > 0:
            curChar = width
            while curChar > -1 and not text[curChar] == " ":
                curChar -= 1
                if curChar == -1:
                    good = False
                    break
            if not good:
                break
            output.append(text[:curChar])
            i -= 1
            text = text[curChar + 1:]
            if len(text) <= width and i > 0:
                output.append(text)
                text = ""
                break
        if len(text) != 0:
            results.append("WILL NOT FIT")
        else:
            for j in output:
                results.append(j)
    else:
        results.append(text)




for r in results:
    print(r)

