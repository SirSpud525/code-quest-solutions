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
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

blue = "blue"
red = "red"

for input in bank:
    strInput = str(input)
    if red in strInput:
        print("red")
    elif blue in strInput:
        print("blue")
    else:
        print("no color found")