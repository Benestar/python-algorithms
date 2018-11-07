"""
Algorithms for minimum spanning trees
"""

from union_find import UnionFind


def kruskal(graph, weights):
    union_find = UnionFind(len(graph))

    for u, v in sorted(weights, key=weights.get):
        if union_find.find(u) != union_find.find(v):
            union_find.union(u, v)

            yield u, v


def prim(graph, weights):
    INF = float('inf')

    values = [INF for _ in graph]
    queue = [(INF, v, None) for v in graph]
    elements = set(graph)

    heapq.heapify(queue)

    while elements:
        _, v, u = heapq.heappop(queue)

        try:
            elements.remove(v)
        except:
            continue

        if u is not None:
            yield u, v

        for u in graph[v]:
            if u in elements and weights[v, u] < values[u]:
                values[u] = weights[v, u]
                heapq.heappush(queue, (values[u], u, v))
