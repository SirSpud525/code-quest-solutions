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
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for triangle in bank:
    sides = triangle.split(", ")
    sides = list(map(int, sides))
    if (sides[0] + sides[1] > sides[2]) and (sides[1] + sides[2] > sides[0]) and (sides[0] + sides[2] > sides[1]):
        if sides[0] == sides[1] == sides[2]:
            print("Equilateral")
        elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Not a Triangle")


