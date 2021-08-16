# Collections Deque
# Written by eyedi

import sys
import bisect
from collections import deque

dq = deque()
dq.append(1)
print(dq)
dq.append(3)
dq.append(2)
dq.append(6)
dq.append(2)
print(dq)

#ret = dq.popleft()
ret = dq.popleft()
print(ret, dq)

ret = dq.pop()
print(ret, dq)
