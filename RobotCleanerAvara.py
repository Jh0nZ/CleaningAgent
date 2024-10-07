# Clase para implementar la búsqueda Avara
import heapq
from RobotCleaner import RobotCleaner

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
