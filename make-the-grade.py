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
    newCases, key = sys.stdin.readline().rstrip().split()
    for test in range(int(newCases)):
      student, answers = sys.stdin.readline().rstrip().split()
      correct = 0
      total = 0
      for answer in range(len(answers)):
        total += 1
        if answers[answer] == key[answer]:
          correct += 1
      grade = (Decimal(correct) / Decimal(total) * Decimal(100)).quantize(Decimal("0.1"), ROUND_HALF_UP)
      output = student + " " + str(grade) + "% "
      letter = "F"
      if grade >= Decimal(90):
        letter = "A"
      elif grade >= Decimal(80):
        letter = "B"
      elif grade >= Decimal(70):
        letter = "C"
      elif grade >= Decimal(60):
        letter = "D"
      output = output + letter
      results.append(output)




for r in results:
  print(r)
