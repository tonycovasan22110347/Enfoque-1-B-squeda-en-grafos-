import random

class MinConflicts:
    def __init__(self, variables, domains, constraints, max_steps):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.max_steps = max_steps

    def conflicts(self, assignment):
        conflict_count = {var: 0 for var in self.variables}
        for var in self.variables:
            for other in self.variables:
                if var != other and not self.constraints(var, assignment[var], other, assignment[other]):
                    conflict_count[var] += 1
        return conflict_count

    def solve(self):
        assignment = {var: random.choice(self.domains[var]) for var in self.variables}
        for _ in range(self.max_steps):
            conflict_count = self.conflicts(assignment)
            if all(count == 0 for count in conflict_count.values()):
                return assignment

            conflicted_vars = [var for var, count in conflict_count.items() if count > 0]
            if not conflicted_vars:
                continue

            var_to_change = random.choice(conflicted_vars)
            best_value = min(self.domains[var_to_change], key=lambda value: self.evaluate_conflict(var_to_change, value, assignment))
            assignment[var_to_change] = best_value

        return None

    def evaluate_conflict(self, var, value, assignment):
        temp_assignment = assignment.copy()
        temp_assignment[var] = value
        return self.conflicts(temp_assignment)[var]

def constraints(var1, value1, var2, value2):
    return value1 != value2

variables = ['A', 'B', 'C']
domains = {
    'A': [1, 2],
    'B': [2, 3],
    'C': [1, 3]
}
max_steps = 100

# Instanciar y resolver el problema con MinConflicts
min_conflicts_solver = MinConflicts(variables, domains, constraints, max_steps)
solution = min_conflicts_solver.solve()

# Imprimir la solución
if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
