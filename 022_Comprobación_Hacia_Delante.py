class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append(v)
        self.edges[v].append(u)

    def get_neighbors(self, node):
        return self.edges.get(node, [])

class PathFinder:
    def __init__(self, graph):
        self.graph = graph

    def is_valid(self, node, path):
        return node not in path

    def forward_check(self, node, path):
        for neighbor in self.graph.get_neighbors(node):
            if self.is_valid(neighbor, path):
                return True
        return False

    def backtrack(self, current_node, goal, path):
        path.append(current_node)

        if current_node == goal:
            return path

        for neighbor in self.graph.get_neighbors(current_node):
            if self.is_valid(neighbor, path) and self.forward_check(neighbor, path):
                result = self.backtrack(neighbor, goal, path)
                if result:
                    return result
        
        path.pop()  
        return None

    def find_path(self, start, goal):
        return self.backtrack(start, goal, [])

grafo = Graph()
grafo.add_edge(1, 2)
grafo.add_edge(1, 3)
grafo.add_edge(2, 4)
grafo.add_edge(2, 5)
grafo.add_edge(3, 6)
grafo.add_edge(4, 7)
grafo.add_edge(5, 7)
grafo.add_edge(6, 7)

path_finder = PathFinder(grafo)
inicio = 1
objetivo = 7
resultado = path_finder.find_path(inicio, objetivo)

if resultado:
    print(f"Camino encontrado: {resultado}")
else:
    print("No se encontró un camino.")
