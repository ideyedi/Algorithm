# /bin/python3
# Written by eyedi
import sys

def MemorizedCutRodAux(p, n, r):
    q = 0
    # Return value, if value is positive
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0
    else:
        q = -sys.maxsize
        for i in range(1, n+1):
            q = max(q, p[i] + MemorizedCutRodAux(p, n-i, r))

    r[n] = q
    print(r)
    return q


def MemorizedCutRod(p, n):
    r = [-sys.maxsize for _ in range(n + 1)]
    print(r)
    return MemorizedCutRodAux(p, n, r)


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
length = 5

ret = MemorizedCutRod(p, length)
print(ret)
