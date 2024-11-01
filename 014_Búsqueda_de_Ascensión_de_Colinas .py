import random

class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def get_neighbors(self, state):
        return [state - 1, state + 1]

    def evaluate(self, state):
        return -abs(state)  

def hill_climbing(problem):
    current = problem.initial_state
    while True:
        neighbors = problem.get_neighbors(current)
        if not neighbors:
            return current
        next_state = max(neighbors, key=lambda state: problem.evaluate(state))
        if problem.evaluate(next_state) <= problem.evaluate(current):
            return current
        current = next_state

if __name__ == "__main__":
    initial_state = random.randint(-10, 10)  
    problem = Problem(initial_state)
    result = hill_climbing(problem)
    print(f"Estado inicial: {initial_state}, Estado óptimo encontrado: {result}")
