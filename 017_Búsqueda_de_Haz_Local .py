class LocalBeamSearch:
    def __init__(self, initial_states, evaluate, neighbors, beam_width):
        self.beam_width = beam_width
        self.current_states = initial_states
        self.evaluate = evaluate
        self.neighbors = neighbors

    def search(self, iterations):
        for _ in range(iterations):
            all_neighbors = []
            for state in self.current_states:
                all_neighbors.extend(self.neighbors(state))
            all_neighbors = list(set(all_neighbors))  
            scored_neighbors = [(state, self.evaluate(state)) for state in all_neighbors]
            scored_neighbors.sort(key=lambda x: x[1], reverse=True)

            self.current_states = [state for state, _ in scored_neighbors[:self.beam_width]]

        return max(self.current_states, key=self.evaluate)

class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def get_neighbors(self, state):
        return [state + i for i in [-1, 1]]  

    def evaluate(self, state):
        return -abs(state) 

initial_states = [0, 1]  
beam_width = 2 
iterations = 10  

problem = Problem(initial_state=0)

local_beam_search = LocalBeamSearch(initial_states, problem.evaluate, problem.get_neighbors, beam_width)

best_solution = local_beam_search.search(iterations)

print("Mejor solución encontrada:", best_solution)
print("Valor de la mejor solución:", problem.evaluate(best_solution))
