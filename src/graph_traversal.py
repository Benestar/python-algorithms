"""
Graph traversal algorithms
"""

from collections import deque


def dfs(graph, v, explored=None):
    queue = deque([(v, None)])
    explored = set() if explored is None else explored

    while queue:
        # pop right side (LIFO)
        v, p = queue.pop()

        if v not in explored:
            yield v, p

            explored.add(v)
            queue.extend((u, v) for u in graph[v])


def bfs(graph, v, explored=None):
    queue = deque([(v, None)])
    explored = set() if explored is None else explored

    while queue:
        # pop left side (FIFO)
        v, p = queue.popleft()

        if v not in explored:
            yield v, p

            explored.add(v)
            queue.extend((u, v) for u in graph[v])


def traverse(graph, algo):
    explored = set()

    for v in graph:
        if v not in explored:
            yield from algo(graph, v, explored)


def topological_sort(graph, preds, roots):
    queue = deque((v, None) for v in roots)

    while queue:
        v, p = queue.pop()

        yield v, p

        for u in graph[v]:
            preds[u] -= 1

            if preds[u] == 0:
                queue.append((u, v))
