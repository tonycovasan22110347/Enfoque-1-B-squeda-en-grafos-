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

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    visited_start = {start}
    visited_goal = {goal}
    queue_start = [(start, [start])]
    queue_goal = [(goal, [goal])]

    while queue_start and queue_goal:

        path_start, current_start = queue_start.pop(0)

        if current_start in visited_goal:
  
            for path_goal, current_goal in queue_goal:
                if current_goal == current_start:
                    return path_start + path_goal[::-1][1:]

        for neighbor in graph.get_neighbors(current_start):
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                queue_start.append((path_start + [neighbor], neighbor))

        path_goal, current_goal = queue_goal.pop(0)

        if current_goal in visited_start:

            for path_start, current_start in queue_start:
                if current_start == current_goal:
                    return path_goal + path_start[::-1][1:]

        for neighbor in graph.get_neighbors(current_goal):
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                queue_goal.append((path_goal + [neighbor], neighbor))

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

    resultado = bidirectional_search(grafo, 1, 6)
    print("Camino encontrado:", resultado)  
