import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

bank=[]
uppers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for text in bank:
    text = list(text)
    for c in range(len(text)):
        if text[c] == "-":
            text[c] = " "
    newText = ""
    for c in text:
        if c in uppers or c in lowers or c == " ":
            newText = newText + c
    newText = newText.split()
    output = ""
    for item in newText:
        output = output + item[0].upper()
    print(output)



#     text = "".join(text.split())
#     text = "".join(text.split("-"))