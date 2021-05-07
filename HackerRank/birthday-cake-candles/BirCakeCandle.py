#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    tallest = 0;
    count = 0;

    for item in candles:
        if tallest == 0:
            tallest = item
            count = count + 1
    
        elif tallest == item:
            count = count + 1

        elif tallest < item:
            count = 1
            tallest = item

    return count


if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)
