class MDP:
    def __init__(self, states, actions, transition_probabilities, rewards, discount_factor):
        self.states = states
        self.actions = actions
        self.transition_probabilities = transition_probabilities
        self.rewards = rewards
        self.discount_factor = discount_factor

    def value_iteration(self, threshold):
        value_function = {state: 0 for state in self.states}
        while True:
            delta = 0
            for state in self.states:
                v = value_function[state]
                value_function[state] = max(self.calculate_action_value(state, action, value_function) for action in self.actions)
                delta = max(delta, abs(v - value_function[state]))
            if delta < threshold:
                break
        return value_function

    def calculate_action_value(self, state, action, value_function):
        return sum(self.transition_probabilities[state][action][next_state] * 
                   (self.rewards[state][action][next_state] + 
                    self.discount_factor * value_function[next_state])
                   for next_state in self.states)

# Ejemplo de uso
if __name__ == "__main__":
    states = ['s1', 's2']
    actions = ['a1', 'a2']
    
    # Probabilidades de transición: P(s' | s, a)
    transition_probabilities = {
        's1': {
            'a1': {'s1': 0.8, 's2': 0.2},
            'a2': {'s1': 0.5, 's2': 0.5}
        },
        's2': {
            'a1': {'s1': 0.1, 's2': 0.9},
            'a2': {'s1': 0.3, 's2': 0.7}
        }
    }
    
    # Recompensas: R(s, a, s')
    rewards = {
        's1': {
            'a1': {'s1': 5, 's2': 10},
            'a2': {'s1': 1, 's2': 2}
        },
        's2': {
            'a1': {'s1': 0, 's2': 3},
            'a2': {'s1': 4, 's2': 1}
        }
    }
    
    discount_factor = 0.9

    mdp = MDP(states, actions, transition_probabilities, rewards, discount_factor)
    value_function = mdp.value_iteration(threshold=0.01)

    print("Función de valor final:", value_function)
