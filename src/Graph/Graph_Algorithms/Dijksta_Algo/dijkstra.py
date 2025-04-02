import heapq


def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest paths from a start node to all other nodes in a graph.
    :param graph: Dictionary representation of the graph {node: [(neighbor, weight), ...]}
    :param start: The starting node
    :return: Dictionary containing shortest distances from start to each node
    """
    pq = [(0, start)]  # Priority queue initialized with (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


