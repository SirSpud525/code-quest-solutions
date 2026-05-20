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
    bank.append((sys.stdin.readline().rstrip()))

for nums in bank:
    nums = nums.split()
    i = len(nums)
    result = ""
    for j in range(i):
        firstDigits = []
        for num in nums:
            firstDigits.append(num[0])
        firstDigits = list(map(int, firstDigits))
        largest = str(max(firstDigits))
        curNum = None
        for num in nums:
            if curNum == None:
                curNum = num
            elif num[0] == largest:
                if int(num + curNum) > int(curNum + num):
                    curNum = num
        nums.remove(curNum)
        result = result + curNum
    if int(result) == 0:
        result = 0
    print(result)