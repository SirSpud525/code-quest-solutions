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
# strinp out inputs from the input channel
cases = int(sys.stdin.readline().rstrip())
for thing in range(cases):
    bank.append((sys.stdin.readline().rstrip()))

for item in bank:
    new = item
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    new = new.replace('$', "")
    dollars, cents = new.split('.')
    cents = int(cents)
    dollars = int(dollars)
    quarters = dollars * 4
    while (25 <= cents):
        cents = cents - 25
        quarters = quarters + 1
    while (10 <= cents):
        cents = cents - 10
        dimes = dimes + 1
    while (5 <= cents):
        cents = cents - 5
        nickels = nickels + 1
    while (1 <= cents):
        cents = cents - 1
        pennies = pennies + 1
    print(item)
    print("Quarters=" + str(quarters))
    print("Dimes=" + str(dimes))
    print("Nickels=" + str(nickels))
    print("Pennies=" + str(pennies))





