def salto_atras_conflictos(nombres, colores):
\
    asignacion = {nombre: None for nombre in nombres}

    def es_valido(nombre, color):
  
        for n, c in asignacion.items():
            if n != nombre and c == color:  
                return False
        return True  

    def asignar_colores(i):

        if i == len(nombres):
            print("Asignación completa y válida:", asignacion)
            return True
        
        nombre_actual = nombres[i]  
        for color in colores:
            if es_valido(nombre_actual, color):
                asignacion[nombre_actual] = color  
                print(f"Asignando {color} a {nombre_actual}")

                if asignar_colores(i + 1):
                    return True 
                print(f"Retrocediendo, quitando asignación de {nombre_actual}")
                asignacion[nombre_actual] = None
        
        return False 

nombres = ["Fernanda", "Emmanuel", "Carlos"]
colores = ["Rojo", "Verde", "Azul"]
tos
if not salto_atras_conflictos(nombres, colores):
    print("No se encontró una asignación válida.")