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


# Clase para implementar la búsqueda en anchura (BFS)
from collections import deque

class RobotCleanerBFS(RobotCleaner):
    def bfs(self, start_x, start_y):
        queue = deque([(start_x, start_y)])  # Cola para la búsqueda en anchura
        self.visited.add((start_x, start_y))  # Marcar el inicio como visitado
        
        while queue:
            x, y = queue.popleft()  # Obtener la primera celda en la cola
            self.level += 1  # Aumentar el nivel de profundidad

            self.clean_and_print(x, y)  # Limpiar la celda y mostrar el estado del árbol
            
            # Movimientos posibles: arriba, abajo, izquierda, derecha
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if self.is_valid_move(next_x, next_y):
                    queue.append((next_x, next_y))  # Agregar la celda a la cola
                    self.visited.add((next_x, next_y))  # Marcar como visitada


# Clase para implementar la búsqueda Avara
import heapq

class RobotCleanerAvara(RobotCleaner):
    def heuristic(self, x, y):
        # Encontrar la celda sucia más cercana usando la distancia de Manhattan
        dirty_cells = [(i, j) for i in range(self.rows) for j in range(self.cols) if self.grid[i][j] == 1]
        if not dirty_cells:
            return float('inf')  # Si no hay más celdas sucias, retornar infinito
        return min(abs(x - i) + abs(y - j) for i, j in dirty_cells)  # Distancia mínima a una celda sucia

    def avara(self, start_x, start_y):
        heap = []
        heapq.heappush(heap, (self.heuristic(start_x, start_y), start_x, start_y))  # Añadir el punto de inicio con su heurística
        self.visited.add((start_x, start_y))  # Marcar el inicio como visitado
        
        while heap:
            self.level += 1  # Aumentar el nivel de profundidad
            _, x, y = heapq.heappop(heap)  # Obtener la celda con la menor heurística

            self.clean_and_print(x, y)  # Limpiar la celda y mostrar el estado del árbol
            
            # Movimientos posibles: arriba, abajo, izquierda, derecha
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if self.is_valid_move(next_x, next_y):
                    heapq.heappush(heap, (self.heuristic(next_x, next_y), next_x, next_y))  # Agregar la celda al heap con su heurística
                    self.visited.add((next_x, next_y))  # Marcar como visitada


# Ejemplo de uso
if __name__ == "__main__":
    # Definición de la cuadrícula (0: celda limpia, 1: celda sucia, -1: celda bloqueada)
    grid = [
        [0, 1, 0, 0],
        [1, 1, 0, -1],
        [0, 0, 1, 0],
        [0, 1, 1, 1]
    ]

    print("Búsqueda Primero en Anchura (BFS):")
    robot_bfs = RobotCleanerBFS(grid)
    robot_bfs.bfs(1, 1)

    print("\nBúsqueda Avara:")
    grid = [
        [0, 1, 0, 0],
        [1, 1, 0, -1],
        [0, 0, 1, 0],
        [0, 1, 1, 1]
    ]  # Reiniciar el grid para el segundo robot
    robot_avara = RobotCleanerAvara(grid)
    robot_avara.avara(1, 1)
