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

output = []
bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    this = sys.stdin.readline().rstrip()
    rows, columns = this.split()
    value = 0
    for i in range(int(rows)):
        nums = sys.stdin.readline().rstrip()
        nums = nums.split()
        for num in nums:
            num = abs(int(num))
            num = pow(num, 2)
            value += num
    value = math.sqrt(value)
    value = round(value + 1e-9, 2)
    value = f"{value:.2f}"
    output.append(value)

for out in output:
    print(out)



