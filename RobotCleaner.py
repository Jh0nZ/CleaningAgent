# Clase base que define el comportamiento general del robot
class RobotCleaner:
    def __init__(self, grid):
        self.grid = grid  # La cuadrícula de limpieza
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()  # Conjunto para rastrear celdas visitadas
        self.path = []  # Para almacenar el camino de limpieza
        self.level = 0  # Nivel de profundidad para la impresión en árbol

    def is_valid_move(self, x, y):
        # Verificar si el movimiento es válido (dentro de los límites y no visitado)
        return (0 <= x < self.rows and 
                0 <= y < self.cols and 
                self.grid[x][y] != -1 and  # -1 representa una celda bloqueada
                (x, y) not in self.visited)

    def print_grid_tree(self):
        indent = "    " * self.level  # Indentar según el nivel actual
        print(f"{indent}Nivel {self.level}:")
        for row in self.grid:
            print(indent, row)  # Imprimir la cuadrícula con indentación para simular el árbol

    def clean_and_print(self, x, y):
        if self.grid[x][y] == 1:
            print(f"Limpieza en la celda: ({x}, {y})")
            self.path.append((x, y))  # Agregar a la ruta de limpieza
            self.grid[x][y] = 0  # Limpiar la celda cambiando a 0
        self.print_grid_tree()  # Mostrar el estado de la cuadrícula después del movimiento
