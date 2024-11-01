import random

class OnlineSearch:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def search(self, problem):
        current_state = self.initial_state
        path = [current_state]

        while not problem.is_goal(current_state):
            action = self.get_next_action(current_state)
            current_state = problem.perform_action(current_state, action)
            path.append(current_state)

        return path

    def get_next_action(self, state):
        return random.choice(['action1', 'action2'])

class Problem:
    def __init__(self, goal_state):
        self.goal_state = goal_state

    def is_goal(self, state):
        return state == self.goal_state

    def perform_action(self, state, action):
        if action == 'action1':
            return state + 1  
        elif action == 'action2':
            return state - 1  

initial_state = 0
goal_state = 5  


problem = Problem(goal_state)

search = OnlineSearch(initial_state)

path = search.search(problem)

print("Camino encontrado:", path)
print("Estado final alcanzado:", path[-1])
