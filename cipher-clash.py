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

bank=[]

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for sentences in bank:
  sentences = sentences[:-1]
  sentences = list(sentences)
  for c in range(len(sentences) - 3):
    if sentences[c] == "\"" and sentences[c + 2] == "\"":
      sentences.pop(c)
      sentences.pop(c)
    if sentences[c] == "]":
      sentences.pop(c+1)
  sentences = "".join(sentences)
  positions, sent1, sent2 = sentences.split("\"")
  positions = list(positions)
  positions.remove("[")
  positions.remove("]")
  positions = "".join(positions)
  pos1, pos2 = positions.split(",")
  sent1 = sent1.split()
  sent2 = sent2.split()
  if Counter(sent1[int(pos1) - 1]) == Counter(sent2[int(pos2) - 1]):
    print("Verified")
  else:
    print("Intercepted")



