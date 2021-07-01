#/bin/python3
# written by eyedi
import sys

'''
Print optimal schdule
'''
def printStations(l: list, op_l: int, n: int):
    i = op_l

    print("Line {}, Station {}".format(i, n + 1))
    for j in range(n, 0, -1):
        i = l[i - 1][j]
        print("Line {}, Station {}".format(i, j))


'''
a: Station cost (matrix, int)
t: Line change cost (matrix, int)
e: Enter cost (line(2) array, int)
x: Exit cost (line(2) array, int)
n: Check station number (int)
'''
def FastestWay(a:list , t: list, e: list, x: list, n: int):
    # Initialize
    s = [[0 for _ in range(6)] for _ in range(2)]
    l = [[-1 for _ in range(6)] for _ in range(2)]

    s[0][0] = e[0] + a[0][0]
    s[1][0] = e[1] + a[1][0]

    # Make optimal cost-map 
    for j in range(1, 6):
        # Line 1 cost-map
        if s[0][j - 1] + a[0][j] <= s[1][j - 1] + t[1][j - 1]+ a[0][j] :
            s[0][j] = s[0][j - 1] + a[0][j]
            l[0][j] = 1
        else:
            s[0][j] = s[1][j - 1] + t[1][j - 1]+ a[0][j]
            l[0][j] = 2

        # Line 2 cost-map
        if s[1][j - 1] + a[1][j] <= s[0][j - 1] + t[0][j - 1]+ a[1][j] :
            s[1][j] = s[1][j - 1] + a[1][j]
            l[1][j] = 2
        else:
            s[1][j] = s[0][j - 1] + t[0][j - 1]+ a[1][j]
            l[1][j] = 1
    
    print(s, l)
    
    # Determine optimal l*, s*
    n = n - 1
    if s[0][n] + x[0] < s[1][n] + x[1]:
        op_s = s[0][n] + x[0]
        op_l = 1
    else:
        op_s = s[1][n] + x[1]
        op_l = 2

    print("Optimal l*: {}, s*: {}".format(op_s, op_l))
    printStations(l, op_l, n)


        
a = [[7,9,3,4,8,4], [8,5,6,4,5,7]]
t = [[2, 1, 1, 3, 4, sys.maxsize],[2, 1, 2, 2, 1, sys.maxsize]]
e = [2,4]
x = [3,2]
n = 6
FastestWay(a, t, e, x, n)
