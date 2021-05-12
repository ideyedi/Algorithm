#/bin/python3
# Written by eyedi
# reference book that Introduction Algorithm 3rd written by Cormen

# Counting sort description
# Not in place and stable algorithm
# It have a linear time complexity

def counting(A, B, k):
    # initialize C list
    C = [0 for i in range(0,k)]
    
    for j in range(1, len(A) - 1):
        C[A[j]] = C[A[j]] + 1

    # C[i] now contains the number of elements equal to i
    for i in range(1, k):
        C[i] = C[i] + C[i-1]

    # C[i] now contains the number of elements less than or equal to i
    for j in range(len(A)-1, 0, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]]-1


A = [2, 5, 3, 0, 2, 3, 0, 3]
B = [0 for i in range(0, 8)]
k = 6
counting(A, B, k)

print(A)
print(B)
