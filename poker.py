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

for nums in bank:
    init = nums
    nums = list(nums)
    nums.sort()
    while "0" in nums:
        nums.remove("0")
    freqs = Counter(nums)
    key = sorted(list(freqs.keys()))
    common = freqs.most_common()
    most = int(common[0][1])
    if len(common) > 1:
        second = int(common[1][1])
    else:
        second = 0
    if most >= 5:
        print(str(init) + " = FIVE OF A KIND")
    elif most == 4:
        print(str(init) + " = FOUR OF A KIND")
    elif most == 3 and second >= 2:
        print(str(init) + " = FULL HOUSE")
    else:
        straight = False
        straightValues = sorted(set(map(int, nums)))
        while 0 in straightValues:
            straightValues.remove(0)
        for i in range(len(straightValues) - 4):
            cont = True
            for j in range(5):
                if straightValues[i] + j == straightValues[i + j]:
                    pass
                else:
                    cont = False
            if cont:
                straight = True
        if straight:
            print(str(init) + " = STRAIGHT")
        elif most == 3:
            print(str(init) + " = THREE OF A KIND")
        elif most == 2 and second == 2:
            print(str(init) + " = TWO PAIR")
        elif most == 2:
            print(str(init) + " = PAIR")
        else:
            print(str(init) + " = " + str(max(list(map(int, nums)))))

