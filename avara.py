import copy

# Definir las direcciones de movimiento: (arriba, abajo, izquierda, derecha)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction_names = ['up', 'down', 'left', 'right']

# Verificar si la posición es válida
def is_valid(x, y, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] != -1

# Verificar si la matriz está completamente limpia
def is_clean(matrix):
    for row in matrix:
        if 1 in row:
            return False
    return True

# Mostrar la matriz
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

# Calcular la distancia Manhattan
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Función que implementa el algoritmo Avara
def greedy_clean(matrix, start_x, start_y):
    # Crear una lista para las posiciones sucias
    dirty_positions = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 1]
    
    # Inicializar el camino y la posición actual
    current_x, current_y = start_x, start_y
    path = []

    while dirty_positions:
        # Encontrar la celda sucia más cercana
        nearest_dirty = None
        nearest_distance = float('inf')

        for (dx, dy) in dirty_positions:
            distance = manhattan_distance(current_x, current_y, dx, dy)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_dirty = (dx, dy)

        # Moverse a la celda más cercana
        if nearest_dirty:
            target_x, target_y = nearest_dirty
            
            while (current_x, current_y) != (target_x, target_y):
                # Determinar la dirección del movimiento
                if current_x < target_x:
                    next_x, next_y = current_x + 1, current_y
                    move = 'down'
                elif current_x > target_x:
                    next_x, next_y = current_x - 1, current_y
                    move = 'up'
                elif current_y < target_y:
                    next_x, next_y = current_x, current_y + 1
                    move = 'right'
                else:
                    next_x, next_y = current_x, current_y - 1
                    move = 'left'

                # Mover a la nueva posición
                if is_valid(next_x, next_y, matrix):
                    current_x, current_y = next_x, next_y
                    path.append(move)

                    # Limpiar la celda si está sucia
                    if matrix[current_x][current_y] == 1:
                        matrix[current_x][current_y] = 0
                        print(f"Cleaned position ({current_x}, {current_y})")
                    
                    print(f"Moved {move} to ({current_x}, {current_y})")
                    print_matrix(matrix)

                else:
                    print(f"Cannot move {move} to ({next_x}, {next_y}) - position is blocked or invalid")
                    break

            # Remover la celda sucia limpiada de la lista
            if nearest_dirty in dirty_positions:
                dirty_positions.remove(nearest_dirty)

    print("All positions cleaned!")
    print(f"Path taken: {path}")

# Matriz de ejemplo: 0 limpio, 1 sucio, -1 bloqueado
matrix = [
    [0, 1, 1],
    [1, -1, 1],
    [1, 1, 0]
]

# Posición inicial del robot
start_x, start_y = 0, 0

# Mostrar el estado inicial
print("Initial matrix:")
print_matrix(matrix)

# Ejecutar el algoritmo Avara para limpiar la matriz
greedy_clean(matrix, start_x, start_y)
