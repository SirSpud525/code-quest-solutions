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

for values in bank:
    func = values.split()[0]
    params = values.split()
    params.pop(0)
    if func == "formatHeight":
        print(params[0] + "\'" + params[1] + "\"")
    elif func == "formatDate":
        while len(params[0]) < 4:
            params[0] = "0" + params[0]
        while len(params[1]) < 2:
            params[1] = "0" + params[1]
        while len(params[2]) < 2:
            params[2] = "0" + params[2]
        print(params[0] + params[1] + params[2])
    else:
        print(",".join(params))


