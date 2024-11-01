import random
import heapq

class Grafo:
    def __init__(self):
        self.aristas = {}

    def agregar_arista(self, u, v, costo=1):
        if u not in self.aristas:
            self.aristas[u] = {}
        self.aristas[u][v] = costo

        if v not in self.aristas:
            self.aristas[v] = {}

    def obtener_vecinos(self, nodo):
        return self.aristas.get(nodo, {}).items()

def bfs(grafo, inicio, objetivo):
    cola = [(inicio, [inicio])]
    while cola:
        (vertice, camino) = cola.pop(0)
        for siguiente in grafo.obtener_vecinos(vertice):
            if siguiente[0] == objetivo:
                return camino + [siguiente[0]]
            else:
                cola.append((siguiente[0], camino + [siguiente[0]]))
    return None

def dfs(grafo, inicio, objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    if inicio == objetivo:
        return [inicio]
    for siguiente in grafo.obtener_vecinos(inicio):
        if siguiente[0] not in visitados:
            camino = dfs(grafo, siguiente[0], objetivo, visitados)
            if camino is not None:
                return [inicio] + camino
    return None

def heuristica(a, b):
    return abs(a - b)

def a_star(grafo, inicio, objetivo):
    conjunto_abierto = []
    heapq.heappush(conjunto_abierto, (0, inicio))
    venido_de = {}
    g_score = {nodo: float('inf') for nodo in grafo.aristas}
    g_score[inicio] = 0
    f_score = {nodo: float('inf') for nodo in grafo.aristas}
    f_score[inicio] = heuristica(inicio, objetivo)

    while conjunto_abierto:
        actual = heapq.heappop(conjunto_abierto)[1]
        if actual == objetivo:
            camino = []
            while actual in venido_de:
                camino.append(actual)
                actual = venido_de[actual]
            return camino[::-1]

        for vecino, costo in grafo.obtener_vecinos(actual):
            tentative_g_score = g_score[actual] + costo
            if tentative_g_score < g_score[vecino]:
                venido_de[vecino] = actual
                g_score[vecino] = tentative_g_score
                f_score[vecino] = tentative_g_score + heuristica(vecino, objetivo)
                if vecino not in [i[1] for i in conjunto_abierto]:
                    heapq.heappush(conjunto_abierto, (f_score[vecino], vecino))

    return None

def algoritmo_genetico(poblacion, funcion_adecuada, generaciones):
    for _ in range(generaciones):
        poblacion = sorted(poblacion, key=funcion_adecuada)
        siguiente_generacion = poblacion[:2]  
        while len(siguiente_generacion) < len(poblacion):
            padres = random.sample(poblacion[:10], 2)
            punto_cruce = random.randint(1, len(padres[0])-1)
            hijo = padres[0][:punto_cruce] + padres[1][punto_cruce:]
            siguiente_generacion.append(hijo)
        
        poblacion = siguiente_generacion
    return poblacion

def retroceso(variables, dominios, restricciones):
    asignacion = {}

    def backtrack():
        if len(asignacion) == len(variables):
            return asignacion
        var = seleccionar_variable_no_asignada(variables, asignacion)
        for valor in dominios[var]:
            if es_consistente(var, valor, asignacion, restricciones):
                asignacion[var] = valor
                resultado = backtrack()
                if resultado is not None:
                    return resultado
                del asignacion[var]
        return None

    return backtrack()

def seleccionar_variable_no_asignada(variables, asignacion):
    for var in variables:
        if var not in asignacion:
            return var
    return None

def es_consistente(var, valor, asignacion, restricciones):
    for (v1, v2), restriccion in restricciones.items():
        if v1 == var and v2 in asignacion and not restriccion(valor, asignacion[v2]):
            return False
        if v2 == var and v1 in asignacion and not restriccion(asignacion[v1], valor):
            return False
    return True


if __name__ == "__main__":
    grafo = Grafo()

    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(1, 3)
    grafo.agregar_arista(2, 4)
    grafo.agregar_arista(3, 4)
    grafo.agregar_arista(4, 5)  

    print("BFS de 1 a 5:", bfs(grafo, 1, 5)) 
    print("DFS de 1 a 5:", dfs(grafo, 1, 5))  
    print("A* de 1 a 5:", a_star(grafo, 1, 5))  
    poblacion = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    funcion_adecuada = lambda x: sum(x)
    print("Resultado del algoritmo genético:", algoritmo_genetico(poblacion, funcion_adecuada, 5))

    variables = ['X1', 'X2']
    dominios = {'X1': [1, 2], 'X2': [3, 4]}
    restricciones = {('X1', 'X2'): lambda x, y: x != y}  
    print("Resultado de retroceso:", retroceso(variables, dominios, restricciones))
