class PolicyIteration:
    def __init__(self, states, actions, transition_probabilities, rewards, discount_factor):
        self.states = states
        self.actions = actions
        self.transition_probabilities = transition_probabilities
        self.rewards = rewards
        self.discount_factor = discount_factor
        self.policy = {state: actions[0] for state in states}
        self.value_function = {state: 0 for state in states}

    def iterate(self, threshold):
        while True:
            self.policy_evaluation()
            stable = self.policy_improvement()
            if stable:
                break

    def policy_evaluation(self):
        while True:
            delta = 0
            for state in self.states:
                v = self.value_function[state]
                action = self.policy[state]
                self.value_function[state] = sum(self.transition_probabilities[state][action][next_state] *
                                                  (self.rewards[state][action][next_state] +
                                                   self.discount_factor * self.value_function[next_state])
                                                  for next_state in self.states)
                delta = max(delta, abs(v - self.value_function[state]))
            if delta < 1e-6:
                break

    def policy_improvement(self):
        stable = True
        for state in self.states:
            old_action = self.policy[state]
            self.policy[state] = max(self.actions, key=lambda action: self.calculate_action_value(state, action))
            if old_action != self.policy[state]:
                stable = False
        return stable

    def calculate_action_value(self, state, action):
        return sum(self.transition_probabilities[state][action][next_state] *
                   (self.rewards[state][action][next_state] + 
                    self.discount_factor * self.value_function[next_state]) 
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

    pi = PolicyIteration(states, actions, transition_probabilities, rewards, discount_factor)
    pi.iterate(threshold=0.01)

    print("Política final:", pi.policy)
    print("Función de valor final:", pi.value_function)
