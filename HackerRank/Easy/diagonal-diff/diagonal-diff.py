#!/bin/python3
import math
import os
import random
import re
import sys

## I don't like setting export value that is 'OUTPUT_PATH'....
n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

sum1 = 0
sum2 = 0

for i in range(n):
    sum1 += arr[i][i]
    sum2 += arr[i][n-i-1] 

print(abs(sum1 - sum2))
