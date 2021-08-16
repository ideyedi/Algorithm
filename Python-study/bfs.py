# /bin/python3
# Written by eyedi
# BFS algorithm in Python

# BFS algorithm
from collections import deque

# G : Matrix
# s : vertex
def BreathFirstSearch(G, s):
    adjacency_nodes = deque([s])
    visited_nodes = [s]

    while adjacency_nodes:
        node = adjacency_nodes.popleft()

        for adjacency_node in G[node]
            if adjacency_node not in visited_nodes:
                visited_node.append(adjacency_node)
                adjacency_nodes.append(adjacency_node)
                # distance[adjacency_node] = distance[node] + 1

    return visited_nodes

G = {
    'A': set(['B', 'F', 'I']),
    'B': ,
    'C': ,
    'D': ,
    'E': ,
    'F': ,
    'G': ,
    'H': ,
    'I': 
}

