# /bin/python3
# reference by Introduction Algorithm 3th writed by Cormen
# Writed by eyedi

import sys

def parent(i):
    return i//2

# function which return left node index about i-value
# python list indexing considered
def left(i):
    return 2*i + 1


# function which return right node index about i-value
# python list indexing considered
def right(i):
    return 2*i + 2


# make list-value to heap
def max_heapify(A, i, length):
    l = left(i)
    r = right(i)

    #print(l, r, A[l], A[r])
    if l <= length and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= length and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        #tmp = A[largest]
        #A[largest] = A[i]
        #A[i] = tmp
        #pyton swap method
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, length)


# make all-value to heap-list
def build_max_heap(A):
    length = len(A)

    # start index is '0'
    for i in range(length//2, -1, -1):
        max_heapify(A,i, length - 1)

# Extract Max heap value
def heap_sort(A):
    # make max-heap
    build_max_heap(A)
    #print("make max-heap {}".format(A))
    
    length = len(A)
    for i in range(length, 1, -1):
        #print("index {} : {} {}".format(i, A[0], A[i-1]))
        A[0], A[i-1] = A[i-1], A[0]
        length -= 1
        max_heapify(A, 0, length - 1)


# increase heap key
def heap_increase_key(A, i, key):
    if key < A[i]:
        print('new key is smaller than current key')

    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

# Insert heap
def max_heap_insert(A, key):
    A.append(-sys.maxsize)
    heap_increase_key(A, len(A)-1, key)


#array = [23, 17, 14, 6, 13, 10, 1, 5, 7, 12]
array = [12, 7, 5, 1, 10, 13, 6, 14, 17, 23]
print(array, len(array))
#max_heap_insert(array, 100)
heap_sort(array)
print(array)
