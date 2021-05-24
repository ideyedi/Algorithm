#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    l = [[] for _ in range(n)]
    lastans = 0
    ret = []

    for q in queries:
        a, x, y = map(int, q)
        idx = (x ^ lastans) % n

        if a == 1:
            l[idx].append(y)
        else:
            lastans = l[idx][y%len(l[idx])]
            ret.append(lastans)

    return ret


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))
    print('\n')
