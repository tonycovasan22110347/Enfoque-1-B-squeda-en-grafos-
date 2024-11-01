class ConflictDirectedBackjumping:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.solution = {}
        self.conflict_graph = {var: [] for var in variables}

    def is_valid(self, var, value):
        for other in self.solution:
            if not self.constraints(var, value, other, self.solution[other]):
                self.conflict_graph[var].append(other)
                return False
        return True

    def backtrack(self):
        if len(self.solution) == len(self.variables):
            return self.solution

        var = self.select_unassigned_variable()
        for value in self.domains[var]:
            if self.is_valid(var, value):
                self.solution[var] = value
                result = self.backtrack()
                if result:
                    return result
                del self.solution[var]  # Asegúrate de eliminar solo si existe en la solución

        if var in self.conflict_graph and self.conflict_graph[var]:
            self.backjump(var)

        return None

    def backjump(self, var):
        # Elimina las variables en conflicto de la solución
        for conflict in self.conflict_graph[var]:
            if conflict in self.solution:
                del self.solution[conflict]

    def select_unassigned_variable(self):
        for var in self.variables:
            if var not in self.solution:
                return var
        return None

def constraints(var1, value1, var2, value2):
    return value1 != value2 

variables = ['A', 'B', 'C']
domains = {
    'A': [1, 2],
    'B': [1, 2],
    'C': [1, 2]
}

csp = ConflictDirectedBackjumping(variables, domains, constraints)
solution = csp.backtrack()

if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
