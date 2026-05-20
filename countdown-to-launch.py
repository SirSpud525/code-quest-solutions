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
    times = int(sys.stdin.readline().rstrip())
    found = False
    toPrint = "ABORT LAUNCH"
    for i in range(times):
        time = sys.stdin.readline().rstrip()
        info = time.split()
        if not found:
            if int(info[2]) <= 1000:
                value = round((float(info[3]) * math.cos(math.radians(int(info[4])))) + 1e-15, 10)
                if abs(value) <= 20:
                    value = round((float(info[3]) * math.sin(math.radians(int(info[4])))) + 1e-15, 10)
                    if abs(value) <= 40:
                        found = True
                        toPrint = info[0] + " " + info[1]
    results.append(toPrint)

for r in results:
    print(r)


