class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)

    def get_neighbors(self, node):
        return self.edges.get(node, [])

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == goal:
        return [start]
    for neighbor in graph.get_neighbors(start):
        if neighbor not in visited:
            path = dfs(graph, neighbor, goal, visited)
            if path is not None:
                return [start] + path
    return None

if __name__ == "__main__":
    grafo = Graph()
    grafo.add_edge(1, 2)
    grafo.add_edge(1, 3)
    grafo.add_edge(2, 4)
    grafo.add_edge(2, 5)
    grafo.add_edge(3, 6)
    grafo.add_edge(4, 7)

    resultado = dfs(grafo, 1, 5)
    print("Camino encontrado en busqueda en profundidad:", resultado)  # Salida esperada: Camino encontrado: [1, 2, 5]
