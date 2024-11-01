import random

class GeneticAlgorithm:
    def __init__(self, population_size, mutate_rate, crossover_rate, evaluate, mutate, crossover):
        self.population_size = population_size
        self.mutate_rate = mutate_rate
        self.crossover_rate = crossover_rate
        self.evaluate = evaluate
        self.mutate = mutate
        self.crossover = crossover

    def run(self, generations):
        population = self.initialize_population()

        for _ in range(generations):
            population = sorted(population, key=self.evaluate, reverse=True)
            next_generation = population[:2]

            while len(next_generation) < self.population_size:
                parent1, parent2 = random.choices(population[:10], k=2) 
                if random.random() < self.crossover_rate:
                    child = self.crossover(parent1, parent2)
                else:
                    child = parent1
                
                if random.random() < self.mutate_rate:
                    child = self.mutate(child)

                next_generation.append(child)

            population = next_generation

        return max(population, key=self.evaluate)

    def initialize_population(self):
        return [self.random_solution() for _ in range(self.population_size)]

    def random_solution(self):
        return random.randint(0, 100)  
    
def evaluate(solution):
    return solution  
def mutate(solution):
    return solution + random.randint(-5, 5)

def crossover(parent1, parent2):
    return (parent1 + parent2) // 2

population_size = 20
mutate_rate = 0.2
crossover_rate = 0.7
generations = 50

ga = GeneticAlgorithm(population_size, mutate_rate, crossover_rate, evaluate, mutate, crossover)

best_solution = ga.run(generations)

print("Mejor solución encontrada:", best_solution)
print("Valor de la mejor solución:", evaluate(best_solution))

