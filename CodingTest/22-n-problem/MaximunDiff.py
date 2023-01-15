#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts UNWEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def maximumDifference(g_nodes, g_from, g_to):
    """
    g_nodes: 그래프 노드 수
    g_from: 그래프 간선 시작 노드 리스트
    g_to: 그래프 간선 끝 노드 리스트
    return: 그래프의 최대 차이
    탐색보다는 undirected니까 맵을 구현하는게 쉬울꺼 같은데
    """
    graph_map = {k: set() for k in range(1, g_nodes+1)}
    path = []
    diff = 0

    for i in range(len(g_from)):
        #print(g_from[i], g_to[i])
        graph_map[g_from[i]].add(g_to[i])

    #print(graph_map)
    print(dfs(graph_map, 1))
    for n in range(1, g_nodes+1):
        ret = dfs(graph_map, n)
        if len(ret) > 1:
            path.append(list(ret))

    for item in path:
        diff = max(diff, max(item) - min(item))

    print(diff)
    return diff



if __name__ == '__main__':
    nodes = 5
    n_from = [1, 1, 2, 2, 3, 4]
    n_to = [2, 3, 3, 4, 4, 5]
    #n_from = [1, 3, 4]
    #n_to = [2, 4, 5]

    ret = maximumDifference(nodes, n_from, n_to)