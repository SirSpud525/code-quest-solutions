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


bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for rhyme in bank:
    people, words = list(map(int, rhyme.split()))
    nerds = []
    for i in range(people):
        nerds.append(i)
    for nerd in nerds:
        start = nerd
        left = nerds.copy()
        while len(left) > 1:
            toElim = start
            toElim += words - 1
            while toElim >= len(left):
                toElim -= len(left)
            left.pop(toElim)
            start = toElim
            if start >= len(left):
                start = 0
        if left[0] == 0:
            print(nerd + 1)



