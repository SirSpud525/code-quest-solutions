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
    bank.append(sys.stdin.readline().rstrip())

for i in bank:
    board = [[i[0], i[1], i[2]], [i[3], i[4], i[5]], [i[6], i[7], i[8]]]
    toOut = "TIE"
    for j in range(3):
        if board[j][0] == board[j][1] and board[j][0] == board[j][2]:
            if board[j][0] == "X":
                toOut = "X WINS"
            elif board[j][0] == "O":
                toOut = "O WINS"
    for k in range(3):
        if board[0][k] == board[1][k] and board[0][k] == board[2][k]:
            if board[0][k] == "X":
                toOut = "X WINS"
            elif board[0][k] == "O":
                toOut = "O WINS"
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[1][1] == "X":
            toOut = "X WINS"
        elif board[1][1] == "O":
            toOut = "O WINS"
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if board[1][1] == "X":
            toOut = "X WINS"
        elif board[1][1] == "O":
            toOut = "O WINS"
    print(i + " = " + toOut)




