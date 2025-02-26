from Graph import GraphList

g = GraphList()
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print_graph()

print("DFS Traversal:")
g.dfs(g.graph, 0)

print("\nBFS Traversal:")
g.bfs(g.graph, 0)

