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

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
bank=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for word in bank:
    yes = True
    for c in word:
        if not c.upper() in alphabet:
            yes = False
    if len(word) < 5 or len(word) > 32:
        yes = False
    if yes:
        print(word)
        row = 1
        for i in range(len(word) - 2):
            line = word[row]
            for j in range(len(word) - 2):
                line = line + " "
            line = line + word[len(word) - row - 1]
            row += 1
            print(line)
        line2 = ""
        for c in range(len(word)):
            line2 = line2 + word[len(word) - c - 1]
        print(line2)
    else:
        print("Not a Calliframe")
