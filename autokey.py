import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

results=[]
uppers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    codeword = sys.stdin.readline().rstrip()
    message = sys.stdin.readline().rstrip()
    for c in message:
        if c in lowers:
            codeword = codeword + c.upper()
    output = ""
    i = 0
    for c in message:
        if c in lowers:
            # print(c)
            # print(codeword[i])
            shift = uppers.index(codeword[i])
            shift = lowers.index(c) + shift
            while shift >= 26:
                shift -= 26
            output = output + uppers[shift]
            i+=1
    results.append(output)


for r in results:
    print(r)

