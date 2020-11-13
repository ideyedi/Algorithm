#!/bin/python3
import math
import os
import random
import re
import sys
from itertools import permutations
from itertools import combinations
#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#
def initialize(s):
# This function is called once before all queries.
    global s_list 
    s_list = list(s)

#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#
def answerQuery(l, r):
# Return the answer for this query modulo 1000000007.
    num = 0
    stack = []
    # set Stack
    for i in range(l, r+1):
        stack.append(s_list[i-1])

    print(list(combinations(stack, 3)))
    return num

if __name__ == '__main__':
    s = input()

    initialize(s)
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        l = int(first_multiple_input[0])
        r = int(first_multiple_input[1])
        result = answerQuery(l, r)
        print(result)

