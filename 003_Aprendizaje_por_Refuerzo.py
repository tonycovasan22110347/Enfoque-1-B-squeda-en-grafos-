import numpy as np

class AprendizajeRefuerzo:
    def __init__(self, acciones, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}
        self.acciones = acciones
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def obtener_q_valor(self, estado, accion):
        return self.q_table.get((estado, accion), 0.0)

    def actualizar_q_valor(self, estado, accion, recompensa, siguiente_estado):
        max_q_siguiente = max(self.obtener_q_valor(siguiente_estado, a) for a in self.acciones)
        q_valor = self.obtener_q_valor(estado, accion)
        self.q_table[(estado, accion)] = q_valor + self.alpha * (recompensa + self.gamma * max_q_siguiente - q_valor)

    def elegir_accion(self, estado):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.acciones)
        return max(self.acciones, key=lambda accion: self.obtener_q_valor(estado, accion))

def simular():
    rl = AprendizajeRefuerzo(acciones=["izquierda", "derecha"])
    for episodio in range(1000):
        estado = "inicial"
        for _ in range(10):
            accion = rl.elegir_accion(estado)
            if accion == "derecha":
                siguiente_estado = "siguiente"
                recompensa = 1
            else:
                siguiente_estado = "inicial"
                recompensa = -1
            rl.actualizar_q_valor(estado, accion, recompensa, siguiente_estado)
            estado = siguiente_estado
            
    # Imprimir la tabla Q después de la simulación
    print("Tabla Q final:")
    for (estado, accion), valor in rl.q_table.items():
        print(f"Estado: {estado}, Acción: {accion}, Valor Q: {valor}")

simular()
