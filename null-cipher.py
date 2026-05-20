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
#strinp out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for case in bank:
    characters = list(case)
    output = ""
    cur = 0
    while cur < len(characters):
        if characters[cur] == "a" or characters[cur] == "e" or characters[cur] == "i" or characters[cur] == "o" or characters[cur] == "u":
            cur += 1
            if not cur == len(characters):
                output = output + characters[cur]
        cur += 1
    print(output)

