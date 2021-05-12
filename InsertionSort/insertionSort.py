#/bin/python3
# Written by eyedi
# reference book that Introduction Algorithm 3rd written by Cormen

# Insertion Sort description
# In place, comparision algoritm

def insertion(A:list):
    length = len(A)
    
    print('Insertion sorting start (length:{})'.format(length))
    for j in range(1, length):
        key = A[j]

        # Insert A[j] into the sorted sequence A[0... j-1]
        # compare key to before value
        i = j - 1

        # 'i' is start zero because programming list index start zero
        while i >= 0 and A[i] > key:
            # 
            A[i+1] = A[i]
            i -= 1
            print("{}: {}".format(j, A))

        A[i+1] = key



A = [5, 2, 4, 6, 1, 3]

print('Before list is {}'.format(A))
insertion(A)
print(A)


