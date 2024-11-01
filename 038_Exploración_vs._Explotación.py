import random

class ExplorationExploitation:
    def __init__(self, states, actions, transition_probabilities, rewards, discount_factor):
        self.states = states
        self.actions = actions
        self.transition_probabilities = transition_probabilities
        self.rewards = rewards
        self.discount_factor = discount_factor
        self.q_table = {state: {action: 0 for action in actions} for state in states}

    def learn(self, episodes, max_steps, epsilon):
        for _ in range(episodes):
            state = random.choice(self.states)
            for _ in range(max_steps):
                action = self.select_action(state, epsilon)
                next_state = self.sample_next_state(state, action)
                reward = self.rewards[state][action][next_state]
                self.update_q_value(state, action, reward, next_state)
                state = next_state

    def select_action(self, state, epsilon):
        if random.random() < epsilon:
            return random.choice(self.actions)  # Exploración
        else:
            return max(self.q_table[state], key=self.q_table[state].get)  # Explotación

    def update_q_value(self, state, action, reward, next_state):
        max_q_next = max(self.q_table[next_state].values())
        self.q_table[state][action] += (reward + self.discount_factor * max_q_next - self.q_table[state][action])

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
    epsilon = 0.1  # Tasa de exploración

    exploration_exploitation = ExplorationExploitation(states, actions, transition_probabilities, rewards, discount_factor)
    exploration_exploitation.learn(episodes, max_steps, epsilon)

    print("Tabla Q final:")
    for state in states:
        print(f"{state}: {exploration_exploitation.q_table[state]}")
