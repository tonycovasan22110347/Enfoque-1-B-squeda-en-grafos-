import numpy as np

class NodoDecision:
    def __init__(self, estado, utilidad=None):
        self.estado = estado
        self.utilidad = utilidad
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def funcion_utilidad(estado):
    return np.random.rand()

def arbol_decision(nodo):
    if not nodo.hijos:
        return nodo.utilidad
    return max(arbol_decision(hijo) for hijo in nodo.hijos)

def analisis_decision():
    raiz = NodoDecision("Inicio")
    for _ in range(5):
        hijo = NodoDecision("Hijo")
        hijo.utilidad = funcion_utilidad(hijo.estado)
        raiz.agregar_hijo(hijo)
    return arbol_decision(raiz)

resultado = analisis_decision()
print("Resultado del análisis de decisión:", resultado)
