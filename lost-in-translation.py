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

valid = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,[]:abcdefghijklmnopqrstuvwxyz")

bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for hexes in bank:
    hexes = hexes.split()
    good = True
    for hex in hexes:
        if not binascii.unhexlify(hex).decode('ASCII') in valid:
            print("INVALID")
            good = False
            break
    if good:
        print("VALID")


