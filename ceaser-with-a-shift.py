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

results = []
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    encoded = sys.stdin.readline().rstrip()
    shifts = sys.stdin.readline().rstrip().split()
    dirs = sys.stdin.readline().rstrip().split()
    shifts = list(map(int, shifts))
    dirs = list(map(int, dirs))
    curShift = 0
    curDir = 0
    decoded = ""
    for c in encoded:
        if c in alphabet:
            index = alphabet.index(c)
            d = dirs[curDir]
            if d == 1:
                index -= shifts[curShift]
            else:
                index += shifts[curShift]
            while index >= 26:
                index -= 26
            while index < 0:
                index += 26
            decoded = decoded + alphabet[index].lower()
            curShift += 1
            curDir += 1
            if curShift >= len(shifts):
                curShift = 0
            if curDir >= len(dirs):
                curDir = 0
        else:
            decoded = decoded + c
    results.append(decoded)

for result in results:
    print(result)