class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)

    def get_neighbors(self, node):
        return self.edges.get(node, [])

def ids(graph, start, goal):
    def dls(node, goal, limit):
        if limit < 0:
            return None
        if node == goal:
            return [node]
        for neighbor in graph.get_neighbors(node):
            path = dls(neighbor, goal, limit - 1)
            if path is not None:
                return [node] + path
        return None

    depth = 0
    while True:
        path = dls(start, goal, depth)
        if path is not None:
            return path
        depth += 1

# Ejemplo de uso
if __name__ == "__main__":
    grafo = Graph()
    grafo.add_edge(1, 2)
    grafo.add_edge(1, 3)
    grafo.add_edge(2, 4)
    grafo.add_edge(2, 5)
    grafo.add_edge(3, 6)
    grafo.add_edge(4, 7)

    resultado = ids(grafo, 1, 5)
    print("Camino encontrado en busqueda en profundidad iterativa:", resultado)  # Salida esperada: Camino encontrado: [1, 2, 5]
