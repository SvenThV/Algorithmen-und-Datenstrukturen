import heapq

def dijkstra(graph, start):
    # Initialisierung
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    shortest_path_tree = {}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Nodes with smaller distances may be processed before, ignore them
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_vertex

    return distances, shortest_path_tree

# Beispielgraph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Startknoten
start_node = 'A'

# Ausführung des Dijkstra-Algorithmus
distances, shortest_path_tree = dijkstra(graph, start_node)

print("Kürzeste Entfernungen:", distances)
print("Kürzester Pfadbaum:", shortest_path_tree)