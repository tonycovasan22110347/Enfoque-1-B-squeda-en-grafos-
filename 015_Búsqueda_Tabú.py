class TabuSearch:
    def __init__(self, initial_solution, evaluate, neighbors, tabu_size=5):
        self.best_solution = initial_solution
        self.best_value = evaluate(initial_solution)
        self.tabu_list = []
        self.evaluate = evaluate
        self.neighbors = neighbors
        self.tabu_size = tabu_size

    def search(self, iterations):
        current_solution = self.best_solution
        for _ in range(iterations):
            neighbor_solutions = self.neighbors(current_solution)
            best_neighbor = None
            best_value = float('-inf')
            for neighbor in neighbor_solutions:
                if neighbor in self.tabu_list:
                    continue
                value = self.evaluate(neighbor)
                if value > best_value:
                    best_value = value
                    best_neighbor = neighbor
            
            if best_neighbor is not None:
                current_solution = best_neighbor
                if self.evaluate(current_solution) > self.best_value:
                    self.best_solution = current_solution
                    self.best_value = self.evaluate(current_solution)

                self.tabu_list.append(current_solution)
                if len(self.tabu_list) > self.tabu_size:
                    self.tabu_list.pop(0)

        return self.best_solution

def evaluate(solution):
    return -abs(solution) 

def neighbors(solution):
    return [solution + i for i in [-1, 1]] 
initial_solution = 0

tabu_search = TabuSearch(initial_solution, evaluate, neighbors)

iterations = 10
best_solution = tabu_search.search(iterations)

print("Mejor solución encontrada:", best_solution)
print("Valor de la mejor solución:", evaluate(best_solution))
