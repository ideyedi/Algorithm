#/bin/python3
# Written by eyedi

import random
import time

import bisect as bs

#example_list = [random.randint(1, 100) for i in range(100)]

# To search using binary search, List must be sorted
#example_list.sort()
# made in upper source
example_list = [3, 4, 4, 6, 8, 9, 9, 9, 10] 

#example_list = [10, 3, 7, 4, 11, 8, 9, 9, 9] 

# Return index which is inserted new value 
print("right : {}".format(bs.bisect_right(example_list, 8)))
print("left : {}".format(bs.bisect_left(example_list, 8)))

# Like 'bisect_right'
print("bisect: {}".format(bs.bisect(example_list, 8)))

# 'insert funcion'..
# insort_left
# insort right, insort

def binarySearch(A:list, item:int) -> int:
    i = bs.bisect_right(A, item)
    index = i - 1
    if A[index] == item:
        return index
    else:
        return -1

print("binarySearch : {}".format(binarySearch(example_list, 8)))

ret = bs.insort_left(example_list, 10)
ret = bs.insort(example_list, 8)
ret = bs.insort_right(example_list, 8)
print(ret, example_list)

# Another use-case
# ref. docs.python
def grade(score, breakpoints=[60, 70, 80, 90], grade='FDCBA'):
    i = bs.bisect(breakpoints, score)
    return grade[i]

#ret = grade("A")
#print(ret)
ret = grade(88)
print(ret)

