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

def checkLeapYear(year):
    year = int(year)
    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def daysSince(day, month, year):
    year = int(year)
    month = int(month)
    day = int(day)
    toReturn = -1
    toReturn += (year-1) * 365
    for i in range(month):
        toReturn += months[i]
    toReturn += day
    for yr in range(year):
        if checkLeapYear(yr):
            toReturn += 1
    if month > 2 and checkLeapYear(year):
        toReturn += 1
    return toReturn

result=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    newCases, size = sys.stdin.readline().rstrip().split()
    files = []
    scores = []
    for i in range(int(newCases)):
        files.append(sys.stdin.readline().rstrip().split())#5 things,  1 is the date
    for file in range(int(newCases)):
        dateParts = files[file][0].split("/")
        age = Decimal(daysSince(27, 4, 2019) - daysSince(dateParts[0], dateParts[1], dateParts[2]))
        if files[file][2] == "AM":
            pass
        else:
            age = age - Decimal("0.5")
        mb = Decimal(files[file][3]) / Decimal(1000)
        score = mb * age
        scores.append(score.quantize(Decimal("0.001"), ROUND_HALF_UP))
    freed = Decimal(0)
    while freed < Decimal(1000000) * Decimal(size) * Decimal("0.25"):
        ind = max(scores)
        ind = scores.index(ind)
        res = files[ind][4] + " " + str(scores[ind])
        result.append(res)
        freed = freed + Decimal(files[ind][3])
        scores[ind] = Decimal(-1)

for r in result:
    print(r)