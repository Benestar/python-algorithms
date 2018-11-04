"""
Graph traversal algorithms
"""

from collections import deque


def dfs(graph, v, explored=None):
    queue = deque([(v, None)])
    explored = set() if explored is None else explored

    while queue:
        v, u = queue.pop()

        if v not in explored:
            yield v, u

            explored.add(v)
            queue.extend((u, v) for u in graph[v])


def bfs(graph, v, explored=None):
    queue = deque([(v, None)])
    explored = set() if explored is None else explored

    while queue:
        v, u = queue.popleft()

        if v not in explored:
            yield v, u

            explored.add(v)
            queue.extend((u, v) for u in graph[v])


def traverse(graph, algo):
    explored = set()

    for v in graph:
        if v not in explored:
            yield from algo(graph, v, explored)
