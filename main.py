from RobotCleanerAvara import RobotCleanerAvara
from RobotCleanerBFS import RobotCleanerBFS
grid = [
    [0, 1, 0, 0],
    [1, 1, 0, -1],
    [0, 0, 1, 0],
    [0, 1, 1, 1]
]

# print("Búsqueda Primero en Anchura (BFS):")
# robot_bfs = RobotCleanerBFS(grid)
# robot_bfs.bfs(0, 0)

print("\nBúsqueda Avara:")
grid = [
    [0, 1, 0, 0],
    [1, 1, 0, -1],
    [0, 0, 1, 0],
    [0, 1, 1, 1]
]  # Reiniciar el grid para el segundo robot
robot_avara = RobotCleanerAvara(grid)
robot_avara.avara(1, 1)