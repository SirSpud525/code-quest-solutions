# Recommended imports for all problems
# Some problems may require more
# IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
import binascii

# list((sys.stdin.readline().rstrip()))

bank = []
# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip()) - 1
key = list((sys.stdin.readline().rstrip()))
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

outWords = []

for line in bank:
    words = line.split()
    for word in words:
        curWord = ""
        chars = word.split('-')
        for char in chars:
            curWord = curWord + key[int(char) - 1]
        outWords.append(curWord)
    output = outWords[0]
    outWords.pop(0)
    for word in outWords:
        output = output + " "
        output = output + word
    print(output)
    outWords = []


