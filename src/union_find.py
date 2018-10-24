"""
Implementation of the union-find data structure
"""

class UnionFind:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1 for _ in range(size)]

    def find(self, a):
        root = a
        parent = self.parent[root]

        # find root
        while parent != root:
            root = parent
            parent = self.parent[root]

        # compress path
        current = a
        while current != root:
            parent = self.parent[current]
            self.parent[current] = root
            current = parent

        return root

    def union(self, a, b):
        a, b = self.find(a), self.find(b)

        # if already united, return root
        if a == b:
            return a

        # a is the larger set
        if self.size[a] < self.size[b]:
            a, b = b, a

        # update parent of b and size of a
        self.parent[b] = a
        self.size[a] = self.size[a] + self.size[b]
