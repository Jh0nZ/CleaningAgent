from collections import deque
from RobotCleaner import RobotCleaner

class RobotCleanerBFS(RobotCleaner):
    def bfs(self, start_x, start_y):
        queue = deque([(start_x, start_y)])  # Cola para la búsqueda en anchura
        self.visited.add((start_x, start_y))  # Marcar el inicio como visitado
        
        # Diccionario para almacenar el árbol de búsqueda (nodo actual: nodo padre)
        tree = {(start_x, start_y): None}
        
        while queue:
            x, y = queue.popleft()  # Obtener la primera celda en la cola
            self.level += 1  # Aumentar el nivel de profundidad
            
            # Limpiar la celda y mostrar el estado actual
            self.clean_and_print(x, y)

            # Movimientos posibles: arriba, abajo, izquierda, derecha
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if self.is_valid_move(next_x, next_y) and (next_x, next_y) not in self.visited:
                    queue.append((next_x, next_y))  # Agregar la celda a la cola
                    self.visited.add((next_x, next_y))  # Marcar como visitada
                    tree[(next_x, next_y)] = (x, y)  # Almacenar el nodo padre

        # Imprimir todo el árbol de búsqueda
        self.print_tree(tree)

    def print_tree(self, tree):
        print("Árbol de búsqueda (hijo -> padre):")
        for child, parent in tree.items():
            if parent is None:
                print(f"{child} (raíz)")
            else:
                print(f"{child} -> {parent}")
