import sys
import math
import string
import itertools
from itertools import permutations
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, getcontext
import binascii

bank=[]
smoothies = {"strawberry swirl" : ["strawberry", "blueberry"], "banana burst" : ["banana", "kiwi", "orange"],
             "tropical tango" : ["kiwi", "orange", "mango", "blueberry"], "mango medley" : ["mango", "strawberry", "blueberry", "banana"]}

#strip out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    ingredients = sys.stdin.readline().rstrip().split("|")
    request = sys.stdin.readline().rstrip()
    good = True
    for ing in smoothies[request]:
        if not ing in ingredients:
            good = False
            break
    if good:
        print("YES")
    else:
        print("NO")



