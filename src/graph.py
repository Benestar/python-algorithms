"""
Graph data structures and algorithms
"""


class AdjacencyListGraph:
    """
    A graph represented by an adjecency list
    """

    def __init__(self, size):
        self.adj_lst = [set() for _ in range(size)]

    def add_vertex(self):
        self.adj_lst.append(set())

    def add_edge(self, u, v):
        self.adj_lst[u].add(v)

    def remove_edge(self, u, v):
        self.adj_lst[u].remove(v)

    def __iter__(self):
        yield from range(len(self.adj_lst))

    def __len__(self):
        return len(self.adj_lst)

    def __getitem__(self, v):
        return self.adj_lst[u]


class AdjacencyMatrixGraph:
    """
    A graph represented by an adjecency matrix
    """

    def __init__(self, size):
        self.adj_mat = [[False for _ in range(size)] for _ in range(size)]

    def add_vertex(self):
        self.adj_mat.append([False for _ in self.adj_mat])

        for row in self.adj_mat:
            row.append(False)

    def add_edge(self, u, v):
        self.adj_mat[u][v] = True

    def remove_edge(self, u, v):
        self.adj_mat[u][v] = False

    def __iter__(self):
        yield from range(len(self.adj_mat))

    def __len__(self):
        return len(self.adj_mat)

    def __getitem__(self, v):
        return set(u for (u, x) in enumerate(self.adj_mat[v]) if x)
