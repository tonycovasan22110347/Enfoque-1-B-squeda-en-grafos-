def heuristic(a, b):
    return abs(a - b)

class Node:
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.g = 0  
        self.h = 0  

    def f(self):
        return self.g + self.h  
class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)

    def get_neighbors(self, node):
        return self.edges.get(node, [])

def a_star(graph, start, goal):
    open_set = []
    closed_set = set()
    start_node = Node(start)
    goal_node = Node(goal)
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

if __name__ == "__main__":

    grafo = Graph()
    grafo.add_edge(1, 2)
    grafo.add_edge(1, 3)
    grafo.add_edge(2, 4)
    grafo.add_edge(2, 5)
    grafo.add_edge(3, 6)
    grafo.add_edge(4, 5)
    grafo.add_edge(5, 6)

    resultado = a_star(grafo, 1, 6)
    print("A* - Camino encontrado:", resultado)
