# Recommended imports for all problems
# Some problems may require more
#IMPORTS
import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

results=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    tasks, works = map(int, sys.stdin.readline().rstrip().split())
    taskList = {}
    for task in range(tasks):
        name, id = sys.stdin.readline().rstrip().split(":")
        taskList[name] = id
    idTimes = {}
    for completed in range(works):
        task, hrs = sys.stdin.readline().rstrip().split(":")
        if taskList[task] in idTimes:
            idTimes[taskList[task]] = idTimes[taskList[task]] + Decimal(hrs)
        else:
            idTimes[taskList[task]] = Decimal(hrs)
    keys = list(map(int, list(idTimes.keys())))
    keys.sort()
    keys = list(map(str, keys))
    totalHrs = Decimal(0)
    for key in keys:
        totalHrs += Decimal(idTimes[key])
    if totalHrs > 24:
        results.append("Error")
    else:
        for key in keys:
            temp = Decimal(idTimes[key]).quantize(Decimal("0.1"), ROUND_HALF_UP)
            results.append(str(key) + ":" + str(temp))


for r in results:
    print(r)