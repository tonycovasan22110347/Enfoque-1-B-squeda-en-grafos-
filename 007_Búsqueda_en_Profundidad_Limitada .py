class Graph: 
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)

    def get_neighbors(self, node):
        return self.edges.get(node, [])

def dls(graph, node, goal, limit, visited=None):
    if visited is None:
        visited = set()
    if limit < 0:
        return None
    visited.add(node)
    if node == goal:
        return [node]
    for neighbor in graph.get_neighbors(node):
        if neighbor not in visited:
            path = dls(graph, neighbor, goal, limit - 1, visited)
            if path is not None:
                return [node] + path
    return None

def depth_limited_search(graph, start, goal, limit):
    return dls(graph, start, goal, limit)

# Ejemplo de uso
if __name__ == "__main__":
    grafo = Graph()
    grafo.add_edge(1, 2)
    grafo.add_edge(1, 3)
    grafo.add_edge(2, 4)
    grafo.add_edge(2, 5)
    grafo.add_edge(3, 6)
    grafo.add_edge(4, 7)

    limite = 2  
    resultado = depth_limited_search(grafo, 1, 5, limite)
    print("Camino encontrado en busqueda en profundidad limitada:", resultado)  # Salida esperada: Camino encontrado: [1, 2, 5]
