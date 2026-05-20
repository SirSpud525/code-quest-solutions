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

letter = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
code = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec",
"Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"]
outputs = []

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank=[]
    newCases = int((sys.stdin.readline().rstrip()))
    for thing in range(newCases):
        bank.append((sys.stdin.readline().rstrip()))
    for item in bank:
        letters = list(item)
        output = ""
        for c in letters:
            if c == ' ':
                output = output[:-1] + " "
            else:
                output = output + code[letter.index(c.upper())] + "-"
        output = output[:-1]
        outputs.append(output)

for out in outputs:
    print(out)


