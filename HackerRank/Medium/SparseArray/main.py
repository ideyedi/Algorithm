"""
!/bin/python3
written by eyedi
"""

import math
import os
import random
import re
import sys

def matchingStrings(strings, queries):
    result = [0 for q in queries]
    print(result)

    for q in range(len(queries)):
        for s in range(len(strings)):
            if queries[q] == strings[s]:
                result[q] += 1
    
    return result


if __name__ == '__main__':
    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))


