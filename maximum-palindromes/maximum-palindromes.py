#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#
def initialize(s):
# This function is called once before all queries.
    global s_list 
    s_list = list(s)
#    print(list(combinations(['1', '2', '3', '4', '5'],2)))
#    print(list(permutations(['a','b', 'c', 'd', 'e'],2)))

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
    string = []
    palin = 0
    drom = 0
    num = 0
    cnt = dict()

    # set list
    for i in range(l, r+1):
        string.append(s_list[i-1])

    for word in string:
        if word not in cnt.keys():
            cnt[word] = 1
        else:
            cnt[word] += 1

    for i in cnt:
        if cnt[i] >= 2:
            palin += 1
            num += cnt[i]//2

        if cnt[i]%2 == 1:
            drom += 1

    a = 1
    b = 1
    for i in range(palin):
         a = a * (num - i)
         b = b * (palin - i)

    if palin == 0:
        return drom
    elif drom == 0:
        return int(a/b)
    else:
        return int(a/b * drom)

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

