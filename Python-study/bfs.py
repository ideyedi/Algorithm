# /bin/python3
# Written by eyedi
# BFS algorithm in Python

# BFS algorithm
from collections import deque

def bfs(graph, start, visited=None):
    q = deque([start])

    visited[start] = True

    while q:
        n = q.popleft()
        
        for i in graph[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    return visited


graph = {0: set([1, 2]),
         1: set([0, 3, 4]),
         2: set([0]),
         3: set([1]),
         4: set([2, 3])}

v = [False for _ in range(len(graph) + 1)]
print(v)
print(bfs(graph, '0', v))

"""
"""
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage:
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

bfs(graph, 'A')
