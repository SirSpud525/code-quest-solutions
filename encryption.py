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

uppers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowers = list("abcdefghijklmnopqrstuvwxyz")
outputs = []

bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    what = sys.stdin.readline().rstrip()
    key = [item.lower() for item in list(sys.stdin.readline().rstrip())]
    newCase = int(sys.stdin.readline().rstrip())
    if what == "ENCRYPT":
        for message in range(newCase):
            message = sys.stdin.readline().rstrip()
            output = ""
            message = list(message)
            for c in message:
                if c == " ":
                    output = output + " "
                elif c in uppers:
                    output = output + key[uppers.index(c)].upper()
                else:
                    output = output + key[lowers.index(c)].lower()
            outputs.append(output)
    else:
        for message in range(newCase):
            message = sys.stdin.readline().rstrip()
            output = ""
            message = list(message)
            for c in message:
                if c == " ":
                    output = output + " "
                elif c in uppers:
                    output = output + uppers[key.index(c.lower())]
                else:
                    output = output + lowers[key.index(c.lower())]
            outputs.append(output)

for out in outputs:
    print(out)




