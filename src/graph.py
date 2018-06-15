"""
Digraph implementation
"""

class Digraph:
    def __init__(self, V=[]):
        self.E = {v: set() for v in V}

    def add_edge(self, u, v):
        if u not in self.E:
            self.E[u] = set()
        if v not in self.E:
            self.E[v] = set()

        self.E[u].add(v)

    def bfs(self, s, t=None):
        visited = set([s])
        dist = {v: float('inf') for v in self.E}
        pred = {v: None for v in G.E}

        dist[s] = 0
        queue = deque([s])

        while queue:
            u = queue.pop()

            for v in self.E[u]:
                if v not in visited:
                    pred[v] = u

                    if v == t:
                        return pred, dist

                    visited.add(v)
                    dist[v] = dist[u] + 1
                    queue.appendleft(v)

        return pred, dist
