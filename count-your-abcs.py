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

for entry in bank:
    letters = list(entry)
    freqs = Counter(letters)
    most = 0
    for key in freqs:
        if freqs[key] > most and not key == ' ':
            most = freqs[key]
    print(most)


