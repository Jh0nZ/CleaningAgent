class RobotCleaner:
    def __init__(self, grid):
        self.grid = grid  # La cuadrícula de limpieza
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()  # Conjunto para rastrear celdas visitadas
        self.path = []  # Para almacenar el camino de limpieza

    def is_valid_move(self, x, y):
        # Verificar si el movimiento es válido (dentro de los límites y no visitado)
        return (0 <= x < self.rows and 
                0 <= y < self.cols and 
                self.grid[x][y] != -1 and  # -1 representa una celda bloqueada
                (x, y) not in self.visited)

    def dfs(self, x, y):
        # Si el robot está en una celda sucia, limpiarla
        if self.grid[x][y] == 1:
            print(f"Limpieza en la celda: ({x}, {y})")
            self.path.append((x, y))  # Agregar a la ruta de limpieza
            self.grid[x][y] = 0  # Limpiar la celda cambiando a 0

        # Marcar la celda como visitada
        self.visited.add((x, y))

        # Movimientos posibles: arriba, abajo, izquierda, derecha
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if self.is_valid_move(next_x, next_y):
                self.dfs(next_x, next_y)

# Ejemplo de uso
if __name__ == "__main__":
    # Definición de la cuadrícula (0: celda limpia, 1: celda sucia, -1: celda bloqueada)
    grid = [
        [0, 1, 0, 0],
        [1, 1, 0, -1],
        [0, 0, 1, 0],
        [0, 1, 1, 1]
    ]

    robot = RobotCleaner(grid)

    # Iniciar la limpieza desde la celda (1, 1)
    robot.dfs(1, 1)

    # Mostrar la ruta de limpieza
    print("Ruta de limpieza:", robot.path)
