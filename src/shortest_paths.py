"""
Shortest path algorithms
"""

import heapq
from graph_traversal import topological_sort


def dijkstra(graph, weights, src):
    INF = float('inf')

    dist = [INF for _ in graph]
    dist[src] = 0

    queue = [(dist[v], v, None) for v in graph]
    elements = set(graph)

    heapq.heapify(queue)

    while elements:
        d, v, p = heapq.heappop(queue)

        try:
            elements.remove(v)
        except:
            continue

        yield v, p, d

        for u in graph[v]:
            if u in elements and dist[v] + weights[v, u] < dist[u]:
                dist[u] = dist[v] + weights[v, u]

                heapq.heappush(queue, (dist[u], u, v))


def bellman_ford(size, weights, src):
    INF = float('inf')

    dist = [INF for _ in range(size)]
    dist[src] = 0

    pred = [None for _ in range(size)]

    for _ in range(size - 1):
        for (u, v) in weights:
            if dist[u] + weights[u, v] < dist[v]:
                dist[v] = dist[u] + weights[u, v]
                pred[v] = u

    for (u, v) in weights:
        if dist[u] + weights[u, v] < dist[v]:
            raise RuntimeError("Negative cycle detected")

    return dist, pred


def floyd_warshall(size, dist):
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


def shortest_path_dag(graph, preds, weights, src):
    INF = float('inf')

    dist = [INF for _ in graph]
    dist[src] = 0

    pred = [None for _ in graph]

    for v, p in topological_sort(graph, preds, [src]):
        yield v, pred[v], dist[v]

        for u in graph[v]:
            if dist[v] + weights[v, u] < dist[u]:
                dist[u] = dist[v] + weights[v, u]
                pred[u] = v
