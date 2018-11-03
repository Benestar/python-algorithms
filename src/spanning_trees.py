"""
Algorithms for minimum spanning trees
"""

from union_find import UnionFind


def kruskal(graph, weights):
    union_find = UnionFind(len(graph))

    for (u, v) in sorted(weights, key=weights.get):
        if union_find.find(u) != union_find.find(v):
            union_find.union(u, v)

            yield (u, v)


def prim(graph, weights):
    pass
