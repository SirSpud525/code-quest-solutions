import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

bank=[]
conversions = {"SECONDS": Decimal(1), "MINUTES": Decimal(60), "HOURS" : Decimal(3600), "DAYS" : Decimal(86400)}

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for times in bank:
    time, starting, ending = times.split()
    output = str(time) + " " + starting + "->"
    time = Decimal(time)
    time = time * conversions[starting]
    time = time / conversions[ending]
    print(output + str(time) + " " + ending)

