import random

class PassiveReinforcementLearning:
    def __init__(self, states, actions, transition_probabilities, rewards, discount_factor):
        self.states = states
        self.actions = actions
        self.transition_probabilities = transition_probabilities
        self.rewards = rewards
        self.discount_factor = discount_factor
        self.value_function = {state: 0 for state in states}
        self.returns = {state: [] for state in states}  # Almacenar retornos para el promedio

    def learn(self, episodes, max_steps):
        for _ in range(episodes):
            state = random.choice(self.states)
            for _ in range(max_steps):
                action = random.choice(self.actions)
                next_state = self.sample_next_state(state, action)
                reward = self.rewards[state][action][next_state]
                # Calcular el retorno para el estado
                self.returns[state].append(reward + self.discount_factor * self.value_function[next_state])
                state = next_state
            
            # Actualizar la función de valor promediando los retornos
            for state in self.states:
                if self.returns[state]:
                    self.value_function[state] = sum(self.returns[state]) / len(self.returns[state])

    def sample_next_state(self, state, action):
        next_states = list(self.transition_probabilities[state][action].keys())
        probabilities = list(self.transition_probabilities[state][action].values())
        return random.choices(next_states, probabilities)[0]

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
    episodes = 1000
    max_steps = 10

    learner = PassiveReinforcementLearning(states, actions, transition_probabilities, rewards, discount_factor)
    learner.learn(episodes, max_steps)

    print("Función de valor final:", learner.value_function)
