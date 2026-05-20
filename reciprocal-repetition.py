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
import re
import binascii

getcontext().prec = 200
# answers = [0,0,3,0,0,6,142857,0,1,0,09,3,769230,714285,6,0,5882352941176470,5,526315789473684210,0,
#            047619,45,4347826086956521739130,6,0,384615384615,037,571428,4482758620689655172413793103,3,
#            032258064516129,0,03,4117647058823529,285714,7,027,631578947368421052]

bank=[]
#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for num in bank:
    num = Decimal(1) / Decimal(num)
    num = str(num).split(".")[1]
    while num[0] == "0":
        num = num[1:len(num)]
    abc = re.search(r'(\d+?)\1+', num)
    if abc:
        print(abc.group(1))
    else:
        print("0")

# for i in range(100):
#     try:
#         print(i)
#         print(Decimal(1)/Decimal(i))
#     except:
#         pass
