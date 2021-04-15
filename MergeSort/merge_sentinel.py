# bin/python3
# 2021.04.15 thurs
# author eyedi

import sys

def merge(A, p, q, r):
    a = q - p + 1
    b = r - q
    # Alloc arr list, set all 0
    arr_L = [0 for i in range(a+1)]
    arr_R = [0 for i in range(b+1)]

    for i in range(a):
        arr_L[i] = A[p+i-1]

    for j in range(b):
        arr_R[j] = A[q+j]

    arr_L[a+1] = sys.maxsize
    arr_R[b+1] = sys.maxsize

    i = j = 1

    for k in range(p, r):
        if arr_L[i] <= arr_R[j]:
            A[k] = arr_L[i]
            i += 1
        else:
            A[k] = arr_R[j]
            j += 1

merge([5,4,3,2,1], 1,2,4)
