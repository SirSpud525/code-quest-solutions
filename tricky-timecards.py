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

bank = []

# strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for person in bank:
    name, *times = person.split(',')
    minutesTotal = 0
    hoursTotal = 0
    for time in times:
        hours, minutes = list(map(int, time.split(':')))
        minutesTotal += minutes
        hoursTotal += hours
    while minutesTotal >= 60:
        minutesTotal -= 60
        hoursTotal += 1
    output = name + "=" + str(hoursTotal) + " hour"
    if hoursTotal != 1:
        output += "s"
    if minutesTotal > 0:
        output += " " + str(minutesTotal) + " minute"
        if minutesTotal != 1:
            output += "s"
    print(output)



