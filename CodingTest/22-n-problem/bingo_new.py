#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getBingoNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY mat
#  2. INTEGER_ARRAY arr


def getBingoNumber(mat, arr):
    # 빙고가 되는 경우의 수
    c_bingo = mat
    r_bingo = list(map(list, zip(*c_bingo)))
    bingo = c_bingo + r_bingo
    input_arr = []

    for i in arr:
        input_arr.append(i)

        for marked in bingo:
            print(marked, input_arr)
            # 여기도 O(n)
            if set(marked).issubset(set(input_arr)):
                print("here")
                return i

    pass


if __name__ == '__main__':
    #mat = [[3, 1, 8], [4, 6, 2], [7, 5, 9]]
    #arr = [5, 4, 8, 7, 6, 1, 9, 2, 3]

    #mat = [[1, 6], [2, 4], [5, 3]]
    #arr = [2, 4, 3, 1, 5, 6]

    mat = [[2, 4, 6], [5, 1, 3]]
    arr = [2, 1, 3, 5, 6, 4]

    result = getBingoNumber(mat, arr)
    print(f"result: {result}")