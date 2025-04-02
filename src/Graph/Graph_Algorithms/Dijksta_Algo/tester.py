from dijkstra import dijkstra

# Test cases
graph1 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

graph2 = {
    'A': [('B', 2)],
    'B': [('A', 2), ('C', 3)],
    'C': [('B', 3)]
}

graph3 = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1)],
    'C': [('A', 5), ('B', 1)]
}

graph4 = {
    'A': [('B', 1)],
    'B': [('A', 1), ('C', 1)],
    'C': [('B', 1)]
}

graph5 = {
    'A': [('B', 3), ('C', 6)],
    'B': [('A', 3), ('C', 2)],
    'C': [('A', 6), ('B', 2)]
}

graph6 = {
    'X': [('Y', 7)],
    'Y': [('X', 7), ('Z', 3)],
    'Z': [('Y', 3)]
}

graph7 = {
    'A': [('B', 10), ('C', 3)],
    'B': [('A', 10), ('C', 1), ('D', 2)],
    'C': [('A', 3), ('B', 1), ('D', 8)],
    'D': [('B', 2), ('C', 8)]
}

graph8 = {
    'P': [('Q', 4), ('R', 1)],
    'Q': [('P', 4), ('R', 2)],
    'R': [('P', 1), ('Q', 2)]
}

graph9 = {
    'M': [('N', 5), ('O', 2)],
    'N': [('M', 5), ('O', 3)],
    'O': [('M', 2), ('N', 3)]
}

graph10 = {
    'S': [('T', 6)],
    'T': [('S', 6)]
}

# Running test cases
print(dijkstra(graph1, 'A'))  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
print(dijkstra(graph2, 'A'))  # {'A': 0, 'B': 2, 'C': 5}
print(dijkstra(graph3, 'A'))  # {'A': 0, 'B': 2, 'C': 3}
print(dijkstra(graph4, 'A'))  # {'A': 0, 'B': 1, 'C': 2}
print(dijkstra(graph5, 'A'))  # {'A': 0, 'B': 3, 'C': 5}
print(dijkstra(graph6, 'X'))  # {'X': 0, 'Y': 7, 'Z': 10}
print(dijkstra(graph7, 'A'))  # {'A': 0, 'B': 4, 'C': 3, 'D': 6}
print(dijkstra(graph8, 'P'))  # {'P': 0, 'Q': 3, 'R': 1}
print(dijkstra(graph9, 'M'))  # {'M': 0, 'N': 5, 'O': 2}
print(dijkstra(graph10, 'S'))  # {'S': 0, 'T': 6}
