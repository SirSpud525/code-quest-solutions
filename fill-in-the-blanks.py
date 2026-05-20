# Recommended imports for all problems
# Some problems may require more
#IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii


results=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    dataLines, templateLines = sys.stdin.readline().rstrip().split()
    data = []
    template = []
    entries = []
    for d in range(int(dataLines)):
        d = sys.stdin.readline().rstrip().split(": ", 1)
        data.append(d[0])
        entries.append(d[1])
    for t in range(int(templateLines)):
        template.append(sys.stdin.readline().rstrip())

    for line in template:
        open = 0
        close = 0
        opened = False
        closed = False
        c = 0
        line = list(line)
        while c < len(line):
            if line[c] == "[":
                open = c
                opened = True
            if line[c] == "]":
                close = c
                closed = True
            if opened and closed:
                toReplace = ""
                for i in range((close - open) - 1):
                    toReplace = toReplace + line[open + 1]
                    line.pop(open + 1)
                line.pop(open)
                # print(line)
                # print(toReplace)
                index = data.index(toReplace)
                line[open] = entries[index]
                # print(line[open])
                c = open
                opened = False
                closed = False
            c += 1
        line = "".join(line)
        results.append(line)

for r in results:
    print(r)





