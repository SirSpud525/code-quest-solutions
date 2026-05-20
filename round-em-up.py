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
#strinp out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for thing in bank:
    dims = thing.split()
    dims = list(map(int, dims))
    output = ""
    if dims[0] % 2 == 1:
        output = output + str(dims[0] + 1)
    else:
        output = output + str(dims[0] + 2)
    if dims[1] % 2 == 1:
        output = output + " " + str(dims[1] + 1)
    else:
        output = output + " " + str(dims[1] + 2)
    if dims[2] % 2 == 1:
        output = output + " " + str(dims[2] + 1)
    else:
        output = output + " " + str(dims[2] + 2)
    print(output)


