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


bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for dna in bank:
    binary = ""
    tides = []
    counter = 0
    for digit in dna:
        if digit == "G" or digit == "C":
            binary = binary + "1"
        else:
            binary = binary + "0"
        counter += 1
        if counter == 7:
            tides.append(binary)
            binary = ""
            counter = 0
    result = ""
    for tide in tides:
        tide = int(tide, 2)
        result = result + chr(tide)
    print(result)


