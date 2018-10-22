"""
Graph data structures and algorithms
"""


class CustomGraph:
    """
    Wrapper for graphs with custom vertex data types
    """

    def __init__(self, graph):
        self.vertices = vertices
        self.graph = graph.with_size(len(vertices))

    @property
    def vertices(self):
        return len(self.vertices)

    def add_vertex(self, v):
        self.vertices.append(v)
        self.graph.add_vertex()

    def remove_vertex(self, v):
        i = self.vertices.find(v)
        del self.vertices[i]
        self.graph.remove_vertex(i)

    def add_edge(self, u, v):
        self.graph.add_edge(
                self.vertices.index(u),
                self.vertices.index(v)
        )

    def remove_edge(self, u, v):
        self.graph.remove_edge(
                self.vertices.index(u),
                self.vertices.index(v)
        )

    def __getitem__(self, v):
        return self.graph[self.vertices.index(v)]


class SetGraph:
    """
    Graph representation based on sets
    """

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    @staticmethod
    def with_size(size):
        self.vertices = set(i for i in range(size))
        self.edges = set()

    @property
    def vertices(self):
        return len(self.vertices)

    def add_vertex(self, v):
        self.vertices.add(v)

    def remove_vertex(self, v):
        self.vertices.remove(v)

        self.edges = set((u, w) for (u, w) in self.edges if u != v and w != v)

    def add_edge(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            raise ValueError("Vertices not from this graph")

        self.edges.add((u, v))

    def remove_edge(self, u, v):
        self.edges.remove((u, v))

    def __getitem__(self, v):
        return set(w for (u, w) in self.edges if u = v)


class AdjacencyListGraph:
    """
    A graph represented by an adjecency list
    """

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    @staticmethod
    def with_size(size):
        return AdjacencyListGraph([set() for _ in range(size)])

    @property
    def vertices(self):
        return len(self.adjacency_list)

    def add_vertex(self):
        self.adjacency_list.append(set())

    def remove_vertex(self, v):
        del self.adjacency_list[v]

        for row in self.adjacency_list:
            row.remove(v)

    def add_edge(self, u, v):
        self.adjacency_list[u].add(v)

    def remove_edge(self, u, v):
        self.adjacency_list[u].remove(v)

    def __getitem__(self, v):
        return self.adjacency_list[u]


class AdjacencyMatrixGraph:
    """
    A graph represented by an adjecency matrix
    """

    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix

    @staticmethod
    def with_size(size):
        return AdjacencyMatrixGraph([[False for _ in range(size)] for _ in range(size)])

    @property
    def vertices(self):
        return len(self.adjacency_list)

    def add_vertex(self):
        self.adjacency_matrix.append([False for _ in self.adjacency_matrix])

        for row in self.adjacency_matrix:
            row.append(False)

    def remove_vertex(self, v):
        del self.adjacency_matrix[v]

        for row in self.adjacency_matrix:
            del row[v]

    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = True

    def remove_edge(self, u, v):
        self.adjacency_matrix[u][v] = False

    def __getitem__(self, v):
        return set(u for (u, x) in self.adjacency_matrix[v] if x)


def bfs(self, graph, start, target=None):
    visited = set([s])
    dist = [float('inf') for _ in range(graph.vertices)]
    pred = [None for _ in range(graph.vertices)]

    dist[start] = 0
    queue = deque([start])

    while queue:
        u = queue.pop()

        for v in graph[u]:
            if v not in visited:
                pred[v] = u

                if v == t:
                    return pred, dist

                visited.add(v)
                dist[v] = dist[u] + 1
                queue.appendleft(v)

    return pred, dist
