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
    region = sys.stdin.readline().rstrip()
    newCase = int(sys.stdin.readline().rstrip())
    infos = {}
    years = []
    for info in range(newCase):
        info = sys.stdin.readline().rstrip()
        money, year = info.split()
        infos[year] = float(money)
        years.append(int(year))
    years.sort()
    print(region + ":")
    for year in years:
        output = str(year) + " "
        money = infos[str(year)]
        money = int(round(money + 1e-9, -3))
        for i in range(int(money / 1000)):
            output = output + "*"
        print(output)

