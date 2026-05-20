import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

bank=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for text in bank:
    output = []
    output.append(text)
    temp = ""
    for i in range(len(text)):
        temp = temp + "-"
    output.append(temp)
    output.append("CHARACTERS: " + str(len(text)))
    output.append("WORDS: " + str(len(text.split())))
    freqs = Counter(text)
    # keys = list(freqs.keys())
    # for key in keys:
    #     output.append(key + ": " + str(freqs[key]))
    commons = freqs.most_common()
    for common in range(len(commons)):
        output.append(commons[common][0] + ": " + str(commons[common][1]))
    # print(commons)
    for r in output:
        print(r)
