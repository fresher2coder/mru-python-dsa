from collections import defaultdict
from collections import deque

class GraphList:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

    def dfs(self, graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in graph[start]:
            if neighbor not in visited:
                self.dfs(graph, neighbor, visited)

    def bfs(self, graph, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(graph[vertex])
