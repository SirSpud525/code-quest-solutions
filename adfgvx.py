# Recommended imports for all problems
# Some problems may require more
# IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import binascii

results = []
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letters = list("ADFGVX")

# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    table = []
    for i in range(6):
        table.append(list(sys.stdin.readline().rstrip()))
    codeword = sys.stdin.readline().rstrip()
    codeChars = list(codeword)
    codeAlph = sorted(codeChars)
    encoded = sys.stdin.readline().rstrip()
    magicNum = len(encoded) % len(codeword)
    original = ""
    encodeAlph = []
    for i in range(len(codeword)):
        encodeAlph.append([])
    for i in range(len(encoded) - magicNum):
        encodeAlph[i % len(codeword)].append(encoded[i])
    indecies = []
    for i in range(magicNum):
        indecies.append(codeAlph.index(codeChars[i]))
    indecies.sort()
    for i in range(magicNum):
        encodeAlph[indecies[i]].append(encoded[len(encoded) - magicNum + i])
    indecies = []
    for i in range(len(codeword)):
        indecies.append(codeAlph.index(codeChars[i]))
    for i in range(len(encoded)):
        original = original + encodeAlph[indecies[i % len(codeword)]][int(i / len(codeword))]
    curSpot = 0
    result = ""
    for i in range(int(len(original) / 2)):
        result = result + table[letters.index(original[curSpot])][letters.index(original[curSpot + 1])]
        curSpot += 2
    results.append(result)

for r in results:
    print(r)


