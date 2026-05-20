# Recommended imports for all problems
# Some problems may require more
#IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import binascii

bank=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for angles in bank:
    angles = angles.split()
    for i in range(3):
        angle = angles[i]
        angle = Decimal(angle)
        angle = angle - Decimal(180)
        while angle < 0:
            angle = angle + Decimal(360)
        while angle >= 360:
            angle = angle - Decimal(360)
        angle.quantize(Decimal("0.01"), ROUND_HALF_UP)
        angle = f"{angle:.2f}"
        angle = f"{angle:0>6}"
        angles[i] = angle
    print(" ".join(angles))