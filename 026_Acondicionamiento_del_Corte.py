class CutConditioning:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.solution = {}

    def is_valid(self, var, value):
        for other in self.solution:
            if not self.constraints(var, value, other, self.solution[other]):
                return False
        return True

    def backtrack(self):
        if len(self.solution) == len(self.variables):
            return self.solution

        var = self.select_unassigned_variable()
        for value in self.domains[var]:
            if self.is_valid(var, value):
                self.solution[var] = value
                self.apply_cut_conditioning(var)
                result = self.backtrack()
                if result:
                    return result
                del self.solution[var]

        return None

    def apply_cut_conditioning(self, var):
        for other in self.variables:
            if other != var:
                self.domains[other] = [value for value in self.domains[other] if self.is_valid(other, value)]

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

cut_conditioning_solver = CutConditioning(variables, domains, constraints)
solution = cut_conditioning_solver.backtrack()

if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
