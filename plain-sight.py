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
    curCases = int(sys.stdin.readline().rstrip())
    answer = ""
    for case in range(curCases):
        curInput = sys.stdin.readline().rstrip()
        word, index = curInput.split('|')
        index = int(index)
        answer = answer + word[index]
    print(answer)