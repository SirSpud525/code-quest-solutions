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

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for word in bank:
    letters = list(word)
    total = 0
    for c in letters:
        index = alphabet.index(c)
        print(c + "=" + str(points[index]))
        total += points[index]
    print("TOTAL=" + str(total))



