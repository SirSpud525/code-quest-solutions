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

results=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    newCases = int(sys.stdin.readline().rstrip())
    info = sys.stdin.readline().rstrip()
    info = info[1:len(info)-1]
    info = info.split("[")
    for i in range(len(info)):
      if i == 0:
        pass
      elif i == len(info) - 1:
        info[i] = info[i].replace("]","")
        info[i] = info[i].split(",")
      else:
        info[i] = info[i].replace("]","")
        info[i] = info[i][:-1]
        info[i] = info[i].split(",")
      # print(info[i])
    info.pop(0)
    # print(info)
    for i in range(newCases):
      person = sys.stdin.readline().rstrip()
      ind = info[0].index(person)
      results.append("Name: " + info[0][ind])
      results.append("Age: " + info[1][ind])
      results.append("Instagram: " + info[2][ind])
      results.append("Twitter: " + info[3][ind])
      results.append("Phone: " + info[4][ind])
      results.append("Email: " + info[5][ind])


for r in results:
  print(r)
