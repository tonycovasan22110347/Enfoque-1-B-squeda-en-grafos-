class CSP:
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
                result = self.backtrack()
                if result:
                    return result
                del self.solution[var]

        return None

    def select_unassigned_variable(self):
        for var in self.variables:
            if var not in self.solution:
                return var
        return None


variables = ['A', 'B', 'C']

domains = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

def constraints(var1, val1, var2, val2):
    return val1 != val2  
csp = CSP(variables, domains, constraints)

solution = csp.backtrack()

if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
