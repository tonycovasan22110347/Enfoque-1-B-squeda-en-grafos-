import random
import math

class SimulatedAnnealing:
    def __init__(self, initial_solution, evaluate, neighbors):
        self.current_solution = initial_solution
        self.current_value = evaluate(initial_solution)
        self.evaluate = evaluate
        self.neighbors = neighbors

    def anneal(self, initial_temp, cooling_rate, stopping_temp):
        temperature = initial_temp
        best_solution = self.current_solution
        best_value = self.current_value
        
        while temperature > stopping_temp:
            neighbor = random.choice(self.neighbors(self.current_solution))
            neighbor_value = self.evaluate(neighbor)

            if neighbor_value > self.current_value or random.uniform(0, 1) < math.exp((neighbor_value - self.current_value) / temperature):
                self.current_solution = neighbor
                self.current_value = neighbor_value
        
            if self.current_value > best_value:
                best_solution = self.current_solution
                best_value = self.current_value

            temperature *= cooling_rate
        
        return best_solution

# Definición de la función de evaluación
def evaluate(solution):
    return -(solution**2) + 10 

def neighbors(solution):
    return [solution + i for i in [-1, 1, -2, 2]]  
initial_solution = 0

initial_temp = 1000  
cooling_rate = 0.95   
stopping_temp = 1     

simulated_annealing = SimulatedAnnealing(initial_solution, evaluate, neighbors)

best_solution = simulated_annealing.anneal(initial_temp, cooling_rate, stopping_temp)

print("Mejor solución encontrada:", best_solution)
print("Valor de la mejor solución:", evaluate(best_solution))
