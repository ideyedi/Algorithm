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
    count = []
    mux = []

    palin = 0
    drom = 0
    num = 0
    n  = 0
    base = 0
    cnt = dict()
    a = 1
    b = 1
    total = 1

    # set list
    for i in range(l, r+1):
        string.append(s_list[i-1])

    # make dictionary
    for word in string:
        if word not in cnt.keys():
            cnt[word] = 1
        else:
            cnt[word] += 1

    for i in cnt:
        count.append(cnt[i]//2)
        mux.append(cnt[i]%2)
        n += 1

    print(count)
    print(mux)

    for i in range(n - 1):
        for j in range(count[i+1]):
            a = a * (count[i] + 1 - j)
            b = b * (count[i+1] - j)
        print(a)
        print(b)

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

