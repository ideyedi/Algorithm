# python3
import heapq

# heap은 list로 표현 가능
heap = []

h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
heapq.heapify(h)
print(h)