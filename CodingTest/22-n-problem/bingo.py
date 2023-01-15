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


def find_mat(mat, val):
    """ mat에서 val의 위치를 찾아서 return """
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == val:
                return i, j
    # 없는 경우는 없다고 가정
    return None


def getBingoNumber(mat, arr):
    """
    mat: N x M matrix
    arr: 순서대로 선택하는 숫자 리스트
    return: 처음으로 빙고가 완성되는 arr value의 값
    """
    # matrix marked check list
    # 동일한 행 n에 속하는 열 m개가 모두 마크
    # 동일한 열 m에 속하는 행 n개가 모두 마크
    # n = m일 경우 대각도 가능, 대각은 문제에서 고려하지 않음
    r_marked = {k: 0 for k in range(len(mat))}
    c_marked = {k: 0 for k in range(len(mat[0]))}

    for val in arr:
        indics = find_mat(mat, val)
        r_marked[indics[0]] += 1
        c_marked[indics[1]] += 1
        if r_marked[indics[0]] == len(mat[0]) or c_marked[indics[1]] == len(mat):
            return val


if __name__ == '__main__':
    #mat = [[3, 1, 8], [4, 6, 2], [7, 5, 9]]
    #arr = [5, 4, 8, 7, 6, 1, 9, 2, 3]
    mat = [[1, 6], [2, 4], [5, 3]]
    arr = [2, 4, 3, 1, 5, 6]
    result = getBingoNumber(mat, arr)
    print(f"result: {result}")