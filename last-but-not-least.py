import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

bank=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for s in bank:
    s = s[1:len(s) - 1]
    if s == "" or set(list(s)) == {' '}:
        print("No Letter Found")
    else:
        c = len(s) - 1
        while s[c] == " ":
            c -= 1
        print(s[c])

