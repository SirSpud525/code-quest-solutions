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

flowers = [
    ["   ", " * ", "   "],
    ["\\  ", " * ", "   "],
    ["\\| ", " * ", "   "],
    ["\\|/", " * ", "   "],
    ["\\|/", " *-", "   "],
    ["\\|/", " *-", "  \\"],
    ["\\|/", " *-", " |\\"],
    ["\\|/", " *-", "/|\\"],
    ["\\|/", "-*-", "/|\\"]
]

bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for num in bank:
    baseNine = ""
    num = int(num)
    if num == 0:
        baseNine = "0"
    while (not num == 0):
        baseNine = str(num % 9) + baseNine
        num = math.floor(num / 9)
    baseNine = list(baseNine)
    top = ""
    mid = ""
    bot = ""
    for digit in baseNine:
        digit = int(digit)
        top = top + flowers[digit][0] + " "
        mid = mid + flowers[digit][1] + " "
        bot = bot + flowers[digit][2] + " "
    top = top.rstrip()
    mid = mid.rstrip()
    bot = bot.rstrip()
    print(top)
    print(mid)
    print(bot)




