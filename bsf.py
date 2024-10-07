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

# Función recursiva que simula los movimientos y genera el árbol de posibles acciones
def dfs_all_paths(matrix, x, y, path, visited, depth=0):
    # Indentar para visualizar el árbol
    indent = "    " * depth

    # Si encontramos una solución (toda la matriz está limpia)
    if is_clean(matrix):
        print(indent + f"Solution found at depth {depth} with path: {path} (Cost: {depth})")
        print_matrix(matrix)
        return True

    # Marcar la posición actual como visitada
    visited.add((x, y))

    # Probar todos los posibles movimientos y mostrar el árbol
    found_solution = False
    print(indent + f"At position ({x}, {y}) with path: {path}")
    
    for i, (dx, dy) in enumerate(directions):
        new_x, new_y = x + dx, y + dy
        
        if is_valid(new_x, new_y, matrix):
            # Crear una copia de la matriz para el nuevo estado
            new_matrix = copy.deepcopy(matrix)
            # Limpiar la celda si está sucia
            if new_matrix[new_x][new_y] == 1:
                new_matrix[new_x][new_y] = 0
            
            print(indent + f"-> Child: Moving {direction_names[i]} to ({new_x}, {new_y})")
            print_matrix(new_matrix)
            
            # Si no hemos visitado la nueva celda, explorarla
            if (new_x, new_y) not in visited:
                # Recursión hacia el siguiente nivel del árbol
                if dfs_all_paths(new_matrix, new_x, new_y, path + [direction_names[i]], visited, depth + 1):
                    found_solution = True
    
    # Deshacer la visita cuando retrocedamos en la búsqueda
    visited.remove((x, y))
    
    return found_solution

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

# Ejecutar DFS para encontrar una solución mostrando todo el árbol
visited = set()
dfs_all_paths(matrix, start_x, start_y, [], visited)
