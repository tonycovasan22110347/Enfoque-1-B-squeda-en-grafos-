class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)

    def get_neighbors(self, node):
        return self.edges.get(node, [])

def graph_search(graph, start, goal, strategy='bfs'):
    if strategy == 'bfs':
        return bfs(graph, start, goal)
    elif strategy == 'dfs':
        return dfs(graph, start, goal)

def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        if vertex == goal:
            return path
        for neighbor in graph.get_neighbors(vertex):
            queue.append((neighbor, path + [neighbor]))
    return None

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
    grafo.add_edge(4, 5)
    grafo.add_edge(5, 6)

    resultado_bfs = graph_search(grafo, 1, 6, strategy='bfs')
    print("Búsqueda en anchura (BFS) - Camino encontrado:", resultado_bfs)

    resultado_dfs = graph_search(grafo, 1, 6, strategy='dfs')
    print("Búsqueda en profundidad (DFS) - Camino encontrado:", resultado_dfs)
