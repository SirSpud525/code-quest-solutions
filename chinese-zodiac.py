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

elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

bank = []
# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for year in bank:
    output = year + " "
    year = int(year)
    if year % 2 == 0:
        output = output + "Yang "
    else:
        output = output + "Yin "

    num = year - 4
    num = num % 10
    num = math.floor(num / 2)
    output = output + elements[num] + " "

    num = year - 4
    num = num % 12
    output = output + animals[num]

    print(output)


