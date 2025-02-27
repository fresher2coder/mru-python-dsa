class GraphMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0] * self.V for _ in range(self.V)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1  # For an undirected graph

    def print_graph(self):
        for row in self.matrix:
            print(row)


