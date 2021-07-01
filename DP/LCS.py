# /bin/python3
# Written by eyedi
dic = {10:"column",20:"diagonal", 30:"row"}

def PrintLCS(b, X, i, j):
    if i < 0 or j < 0:
        return ""
    if b[i][j] == 20:
        PrintLCS(b, X, i-1, j-1)
        print(X[i])
    elif b[i][j] == 10:
        PrintLCS(b, X, i-1, j)
    else:
        PrintLCS(b, X, i, j-1)


# LCS (Longest common subsequence)
def LCSLen(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0 for _ in range(n)] for _ in range(m)]
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i+1][j+1] = c[i][j] + 1
                b[i][j] = 20
            elif c[i][j+1] >= c[i+1][j]:
                c[i+1][j+1] = c[i][j+1]
                b[i][j] = 10
            else:
                c[i+1][j+1] = c[i+1][j]
                b[i][j] = 30

    #print(b)
    #print("-"*100)
    #print(c)
    print(b)
    PrintLCS(b, X, m-1, n-1)


str1 = "ABCBDAB"
str2 = "BDCABA"
LCSLen(str1, str2)
