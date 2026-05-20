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

upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower = list("abcdefghijklmnopqrstuvwxyz")
nums = list("1234567890")

bank = []
# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for password in bank:
    if len(password) >= 8:
        chars = list(password)
        sections = [0, 0, 0, 0]
        for c in chars:
            if c in upper:
                sections[0] = 1
            elif c in lower:
                sections[1] = 1
            elif c in nums:
                sections[2] = 1
            else:
                sections[3] = 1
        counts = Counter(sections)
        if counts[1] < 3:
            print("INVALID")
        else:
            valid = True
            i = 1
            for c in range(len(chars) - 2):
                if chars[i - 1] == chars[i] and chars[i] == chars[i + 1]:
                    valid = False
                i += 1
            if valid:
                print("VALID")
            else:
                print("INVALID")

    else:
        print("INVALID")



