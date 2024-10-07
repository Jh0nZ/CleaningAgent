import copy

# Definir las direcciones de movimiento: (arriba, abajo, izquierda, derecha)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction_names = ['arriba', 'abajo', 'izquierda', 'derecha']

# Verificar si la posición es válida
def es_valida(x, y, matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return 0 <= x < filas and 0 <= y < columnas y matriz[x][y] != -1

# Verificar si la matriz está completamente limpia
def esta_limpia(matriz):
    for fila in matriz:
        if 1 in fila:
            return False
    return True

# Mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

# Función recursiva que simula los movimientos y genera el árbol de posibles acciones
def dfs_todos_caminos(matriz, x, y, camino, visitado, profundidad=0):
    # Indentar para visualizar el árbol
    indentacion = "    " * profundidad

    # Si encontramos una solución (toda la matriz está limpia)
    if esta_limpia(matriz):
        print(indentacion + f"Solución encontrada en profundidad {profundidad} con camino: {camino} (Costo: {profundidad})")
        mostrar_matriz(matriz)
        return True

    # Marcar la posición actual como visitada
    visitado.add((x, y))

    # Probar todos los posibles movimientos y mostrar el árbol
    solucion_encontrada = False
    print(indentacion + f"En posición ({x}, {y}) con camino: {camino}")
    
    for i, (dx, dy) in enumerate(directions):
        nuevo_x, nuevo_y = x + dx, y + dy
        
        if es_valida(nuevo_x, nuevo_y, matriz):
            # Crear una copia de la matriz para el nuevo estado
            nueva_matriz = copy.deepcopy(matriz)
            # Limpiar la celda si está sucia
            if nueva_matriz[nuevo_x][nuevo_y] == 1:
                nueva_matriz[nuevo_x][nuevo_y] = 0
            
            print(indentacion + f"-> Hijo: Moviéndose {direction_names[i]} a ({nuevo_x}, {nuevo_y})")
            mostrar_matriz(nueva_matriz)
            
            # Si no hemos visitado la nueva celda, explorarla
            if (nuevo_x, nuevo_y) no está en visitado:
                # Recursión hacia el siguiente nivel del árbol
                if dfs_todos_caminos(nueva_matriz, nuevo_x, nuevo_y, camino + [direction_names[i]], visitado, profundidad + 1):
                    solucion_encontrada = True
    
    # Deshacer la visita cuando retrocedamos en la búsqueda
    visitado.remove((x, y))
    
    return solucion_encontrada

# Matriz de ejemplo: 0 limpio, 1 sucio, -1 bloqueado
matriz = [
    [0, 1, 1],
    [1, -1, 1],
    [1, 1, 0]
]

# Posición inicial del robot
inicio_x, inicio_y = 0, 0

# Mostrar el estado inicial
print("Matriz inicial:")
mostrar_matriz(matriz)

# Ejecutar DFS para encontrar una solución mostrando todo el árbol
visitado = set()
dfs_todos_caminos(matriz, inicio_x, inicio_y, [], visitado)
