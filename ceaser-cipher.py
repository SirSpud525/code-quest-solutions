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

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases * 2):
    bank.append((sys.stdin.readline().rstrip()))

curInd = 0

for i in range(cases):
    shift = int(bank[curInd])
    curInd += 1
    encrypted = list(bank[curInd])
    curInd += 1
    output = ""
    for letter in encrypted:
        if letter == " ":
            output = output + " "
        else:
            newInd = alphabet.index(letter.upper()) - shift
            if shift >=0:
                while newInd < 0:
                    newInd = newInd + 26
            else:
                while newInd > 0:
                    newInd = newInd - 26
            output = output + alphabet[newInd].lower()
    print(output)



