def backtrack(start, combination, n, k, results):
    if len(combination) == k:
        results.append(combination[:])  
        return
    
    for i in range(start, n + 1):
        combination.append(i)  
        backtrack(i + 1, combination, n, k, results)  
        combination.pop() 

def generate_combinations(n, k):
    results = []
    backtrack(1, [], n, k, results)
    return results

n = 5 
k = 3 
combinations = generate_combinations(n, k)

print("Combinaciones de", k, "números de 1 a", n, "son:")
for combo in combinations:
    print(combo)
