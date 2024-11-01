def calcular_utilidad(decision, valor):
    
    return valor * 10   
decisiones = {
    "Jose": {"decisión": "Invertir", "valor": 8},  
    "Juan": {"decisión": "Ahorrar", "valor": 6},  
    "Angel": {"decisión": "Gastar", "valor": 5}      
}

for nombre, info in decisiones.items():
    decision = info["decisión"]
    valor = info["valor"]
    utilidad = calcular_utilidad(decision, valor)  
    print(f"{nombre} tomó la decisión de {decision} con una utilidad de {utilidad}.")