# Recommended imports for all problems
# Some problems may require more
# IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

results = []

# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    t = int(sys.stdin.readline().rstrip())
    table = []
    for dirs in range(t):
        toAppend = sys.stdin.readline().rstrip()
        toAppend = toAppend[1:len(toAppend) - 1]
        toAppend = toAppend.split(", ")
        table.append(toAppend)
    tape = sys.stdin.readline().rstrip().split()

    pos = math.floor(len(tape) / 2)
    steps = int(sys.stdin.readline().rstrip())
    state = "A"
    for i in range(steps):
        for option in table:
            if option[0] == state and option[1] == tape[pos]:
                tape[pos] = option[2]
                if option[3] == "L":
                    pos -= 1
                else:
                    pos += 1
                state = option[4]
                break
    results.append(" ".join(tape))

for r in results:
    print(r)