class Node:
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.g = 0
        self.h = 0

    def f(self):
        return self.g + self.h


def heuristic(a, b):
    return abs(a - b)


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


def a_star(graph, start, goal):
    open_set = []
    closed_set = set()
    start_node = Node(start)
    open_set.append(start_node)

    while open_set:
        current_node = min(open_set, key=lambda node: node.f())
        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        open_set.remove(current_node)
        closed_set.add(current_node.state)

        for neighbor in graph.get_neighbors(current_node.state):
            if neighbor in closed_set:
                continue
            neighbor_node = Node(neighbor)
            tentative_g = current_node.g + 1

            if neighbor_node not in open_set:
                open_set.append(neighbor_node)
            elif tentative_g >= neighbor_node.g:
                continue

            neighbor_node.parent = current_node
            neighbor_node.g = tentative_g
            neighbor_node.h = heuristic(neighbor_node.state, goal)

    return None


def ao_star(graph, start, goal):
    def recursive_ao(node, visited):
        if node.state == goal:
            return [node.state]
        visited.add(node.state)  

        for neighbor in graph.get_neighbors(node.state):
            if neighbor in visited:
                continue
            path = recursive_ao(Node(neighbor), visited)
            if path:
                return [node.state] + path
        
        visited.remove(node.state) 
        return None

    return recursive_ao(Node(start), set())


if __name__ == "__main__":

    grafo = Graph()
    grafo.add_edge(1, 2)
    grafo.add_edge(1, 3)
    grafo.add_edge(2, 4)
    grafo.add_edge(2, 5)
    grafo.add_edge(3, 6)
    grafo.add_edge(4, 7)
    grafo.add_edge(5, 7)
    grafo.add_edge(6, 7)

    inicio = 1
    objetivo = 7
    resultado_a_star = a_star(grafo, inicio, objetivo)

    if resultado_a_star:
        print("Camino encontrado A*:", resultado_a_star)
    else:
        print("No se encontró un camino con A*.")

    resultado_ao_star = ao_star(grafo, inicio, objetivo)

    
    if resultado_ao_star:
        print("Camino encontrado AO*:", resultado_ao_star)
    else:
        print("No se encontró un camino con AO*.")
