"""
Graph traversal algorithms
"""

from collections import deque

class LifoQueue(deque):

    def get(self):
        return self.pop()

class FifoQueue(deque):

    def get(self):
        return self.popleft()


def explore(graph, queue, explored):
    while queue:
        v = queue.get()

        if v not in explored:
            yield v
            
            explored.add(v)
            queue.extend(graph[v])
    

def traverse(graph, queue):
    explored = set()

    for v in graph:
        if v not in explored:
            queue.append(v)

            yield from explore(graph, queue, explored)

def dfs(graph):
    yield from traverse(graph, LifoQueue())

def bfs(graph):
    yield from traverse(graph, FifoQueue())
