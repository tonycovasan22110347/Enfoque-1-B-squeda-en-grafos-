class Outcome:
    def __init__(self, utility, probability):
        self.utility = utility
        self.probability = probability

class DecisionNode:
    def __init__(self, decision, outcomes):
        self.decision = decision  
        self.outcomes = outcomes   
class DecisionNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def expected_value(self):
        return sum(node.decision * sum(outcome.utility * outcome.probability for outcome in node.outcomes) for node in self.nodes)

outcomes1 = [Outcome(10, 0.5), Outcome(20, 0.5)]  
outcomes2 = [Outcome(15, 0.3), Outcome(25, 0.7)]  

node1 = DecisionNode(1, outcomes1)  
node2 = DecisionNode(2, outcomes2)  

network = DecisionNetwork()
network.add_node(node1)
network.add_node(node2)

expected_value = network.expected_value()
print(f"El valor esperado de la red de decisiones es: {expected_value}")
