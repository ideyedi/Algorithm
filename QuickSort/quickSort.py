#/bin/python3
# Written by eyedi
# reference book that Introduction Algorithm 3rd written by Cormen

# Quick Sort description
# Divide-Conquer and inplace algorithm

# parameter
# A is un-sorted list
# p is start index number
# r is end index number
def partion(A:list, p:int, r:int):
    # x is pivot value
    x = A[r]
    i = p - 1

    # bigger value keep stable position
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]


    A[i+1], A[r] = A[r], A[i+1]

    return i+1


def quicksort(A:list, p:int, r:int):
    # terminated point
    if p < r:
        q = partion(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


A = [3, 1, 2, 3, 4, 1]

print(A)
#partion(A, 0, len(A)-1)
quicksort(A, 0, len(A)-1)
print(A)
