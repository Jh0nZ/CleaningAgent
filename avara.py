import copy

# Definir las direcciones de movimiento: (arriba, abajo, izquierda, derecha)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction_names = ['arriba', 'abajo', 'izquierda', 'derecha']

# Verificar si la posición es válida
def es_valida(x, y, matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return 0 <= x < filas and 0 <= y < columnas and matriz[x][y] != -1

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

# Calcular la distancia Manhattan
def distancia_manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Función que implementa el algoritmo Avara
def limpiar_greedy(matriz, start_x, start_y):
    # Crear una lista para las posiciones sucias
    posiciones_sucias = [(i, j) for i in range(len(matriz)) for j in range(len(matriz[0])) if matriz[i][j] == 1]
    
    # Inicializar el camino y la posición actual
    x_actual, y_actual = start_x, start_y
    camino = []

    while posiciones_sucias:
        # Encontrar la celda sucia más cercana
        mas_cercano = None
        distancia_mas_cercana = float('inf')

        for (dx, dy) in posiciones_sucias:
            distancia = distancia_manhattan(x_actual, y_actual, dx, dy)
            if distancia < distancia_mas_cercana:
                distancia_mas_cercana = distancia
                mas_cercano = (dx, dy)

        # Moverse a la celda más cercana
        if mas_cercano:
            x_destino, y_destino = mas_cercano
            
            while (x_actual, y_actual) != (x_destino, y_destino):
                # Determinar la dirección del movimiento
                if x_actual < x_destino:
                    siguiente_x, siguiente_y = x_actual + 1, y_actual
                    movimiento = 'abajo'
                elif x_actual > x_destino:
                    siguiente_x, siguiente_y = x_actual - 1, y_actual
                    movimiento = 'arriba'
                elif y_actual < y_destino:
                    siguiente_x, siguiente_y = x_actual, y_actual + 1
                    movimiento = 'derecha'
                else:
                    siguiente_x, siguiente_y = x_actual, y_actual - 1
                    movimiento = 'izquierda'

                # Mover a la nueva posición
                if es_valida(siguiente_x, siguiente_y, matriz):
                    x_actual, y_actual = siguiente_x, siguiente_y
                    camino.append(movimiento)

                    # Limpiar la celda si está sucia
                    if matriz[x_actual][y_actual] == 1:
                        matriz[x_actual][y_actual] = 0
                        print(f"Limpio la posicion ({x_actual}, {y_actual})")
                    
                    print(f"Se movio {movimiento} a ({x_actual}, {y_actual})")
                    mostrar_matriz(matriz)

                else:
                    print(f"No se puede mover {movimiento} a ({siguiente_x}, {siguiente_y}) - posicion bloqueada o invalida")
                    break

            # Remover la celda sucia limpiada de la lista
            if mas_cercano in posiciones_sucias:
                posiciones_sucias.remove(mas_cercano)

    print("¡Todas las posiciones fueron limpiadas!")
    print(f"Camino recorrido: {camino}")

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

# Ejecutar el algoritmo Avara para limpiar la matriz
limpiar_greedy(matriz, inicio_x, inicio_y)
