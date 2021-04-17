# bin/python3
# 2021.04.15 thu
# Merge sort not using sentienl value
# Add if condition and copy extra list 
# author eyedi

import sys

def merge(A, p, q, r):
    a = q - p + 1
    b = r - q
    # Alloc arr list, set all 0
    # Don't make sentienl list sector
    arr_L = [0 for i in range(a)]
    arr_R = [0 for i in range(b)]

    for i in range(a):
        arr_L[i] = A[p+i-1]

    for j in range(b):
        arr_R[j] = A[q+j]

    #print(arr_L, arr_R)

    # list index start to zero, 0
    i = j = 0 
    for k in range(p-1, r):
#''''''' Compare subset end point ''''
        if i >= a:
            A[k:r] = arr_R[j:b]
            break
        
        if j >= b:
            A[k:r] = arr_L[i:a]
            break
#''''''''
        if arr_L[i] <= arr_R[j]:
            A[k] = arr_L[i]
            i += 1
        else:
            A[k] = arr_R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    

A = [14,10,9,20,50,43,20,100,37]
print(A)
#merge(A, 1, 5, 9)
merge_sort(A, 1, len(A));
print(A)
