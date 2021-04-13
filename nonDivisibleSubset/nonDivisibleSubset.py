#/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    mod_list = []
    
    for i in range(len(s)):
        mod_list.append(s[i]%k)
	
    #print(mod_list)
    #Maybe we make dictionary type ..?? mod 0 : count, mod 1 : count .. and so on..

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
s = list(map(int, input().rstrip().split()))

result = nonDivisibleSubset(k, s)
print(result)
