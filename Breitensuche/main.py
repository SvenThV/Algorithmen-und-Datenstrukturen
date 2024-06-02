from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node, neighbor):
        self.graph[node].append(neighbor)

    def breitensuche(self, start):
        # Eine Warteschlange für die Knoten, die noch untersucht werden müssen
        queue = deque([start])
        # Ein Set zur Überprüfung, welche Knoten bereits besucht wurden
        visited = set()

        while queue:
            # Den ersten Knoten aus der Warteschlange entfernen
            node = queue.popleft()
            if node not in visited:
                # Den aktuellen Knoten als besucht markieren und ausgeben
                print(node, end=" ")
                visited.add(node)

                # Alle benachbarten Knoten, die noch nicht besucht wurden, zur Warteschlange hinzufügen
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Beispiel für die Verwendung der Klasse
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Breitensuche (BFS) ab Knoten 2:")
g.breitensuche(2)