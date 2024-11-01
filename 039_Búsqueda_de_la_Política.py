import random

class PolicySearch:
    def __init__(self, states, actions, transition_probabilities, rewards, discount_factor):
        self.states = states
        self.actions = actions
        self.transition_probabilities = transition_probabilities
        self.rewards = rewards
        self.discount_factor = discount_factor
        self.policy = {state: random.choice(actions) for state in states}

    def search(self, iterations):
        for _ in range(iterations):
            self.policy_evaluation()
            self.policy_improvement()

    def policy_evaluation(self):
        value_function = {state: 0 for state in self.states}
        for state in self.states:
            action = self.policy[state]
            value_function[state] = sum(
                self.transition_probabilities[state][action][next_state] *
                (self.rewards[state][action][next_state] + 
                 self.discount_factor * value_function.get(next_state, 0))
                for next_state in self.states
            )
        self.value_function = value_function  # Guardar el valor calculado

    def policy_improvement(self):
        for state in self.states:
            old_action = self.policy[state]
            self.policy[state] = max(self.actions, key=lambda action: self.calculate_action_value(state, action))
            if old_action != self.policy[state]:
                print(f"Updated policy for state {state} from {old_action} to {self.policy[state]}")

    def calculate_action_value(self, state, action):
        return sum(
            self.transition_probabilities[state][action][next_state] *
            (self.rewards[state][action][next_state] + 
             self.discount_factor * self.value_function.get(next_state, 0))
            for next_state in self.states
        )

# Ejemplo de uso
if __name__ == "__main__":
    states = ['s1', 's2']
    actions = ['a1', 'a2']

    transition_probabilities = {
        's1': {
            'a1': {'s1': 0.7, 's2': 0.3},
            'a2': {'s1': 0.4, 's2': 0.6}
        },
        's2': {
            'a1': {'s1': 0.5, 's2': 0.5},
            'a2': {'s1': 0.2, 's2': 0.8}
        }
    }

    rewards = {
        's1': {
            'a1': {'s1': 10, 's2': 5},
            'a2': {'s1': 0, 's2': 1}
        },
        's2': {
            'a1': {'s1': 3, 's2': 7},
            'a2': {'s1': 1, 's2': 4}
        }
    }

    discount_factor = 0.9
    iterations = 100

    policy_search = PolicySearch(states, actions, transition_probabilities, rewards, discount_factor)
    policy_search.search(iterations)

    print("Política final:")
    for state in states:
        print(f"{state}: {policy_search.policy[state]}")

