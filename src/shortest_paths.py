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


def bellman_ford(graph, weights, src):
    INF = float('inf')

    dist = [INF for _ in graph]
    dist[src] = 0

    queue = deque([(0, src, None)])
    elements = set([src])

    while elements:
        d, v, p = queue.popleft()

        elements.remove(v)

        yield v, p, d

        for u in graph[v]:
            if dist[v] + weights[v, u] < dist[u]:
                dist[u] = dist[v] + weights[v, u]

                if u not in elements:
                    queue.append((dist[u], u, v))


def bellman_ford_negative_cycles(graph, weights, src):
    INF = float('inf')

    dist = [INF for _ in graph]
    dist[src] = 0

    pop_queue, push_queue = deque([(0, src, None)]), deque()
    pop_elements, push_elements = set([src]), set()

    for _ in range(len(graph) - 1):
        while pop_elements:
            d, v, p = pop_queue.popleft()
            pop_elements.remove(v)

            yield v, p, d

            for u in graph[v]:
                if dist[v] + weights[v, u] < dist[u]:
                    dist[u] = dist[v] + weights[v, u]

                    if u not in push_elements:
                        push_queue.append((dist[u], u, v))
                        push_elements.add(u)

        pop_queue, push_queue = push_queue, pop_queue
        pop_elements, push_elements = push_elements, pop_elements

    if pop_queue:
        raise RuntimeError("Negative cycle detected")


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
