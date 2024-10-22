import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import func

G = nx.Graph()

# Строим метро
stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(stations)

# Связи между станциями с расстояниями
connections = [
    ('A', 'B', 5),
    ('A', 'C', 10),
    ('B', 'D', 3),
    ('B', 'D', 2),  
    ('D', 'F', 4),
    ('G', 'D', 6),
    ('C', 'D', 1),
    ('D', 'E', 2),
    ('E', 'F', 3),
    ('F', 'G', 8),
    ('F', 'H', 7),
    ('G', 'H', 5)
]
G.add_weighted_edges_from(connections)


# Анализ графа
print(f"\nКоличество вершин: {G.number_of_nodes()}")
print(f"Количество ребер: {G.number_of_edges()}\n")
print("Степени вершин:")
degree_dict = dict(G.degree())
for node, degree in degree_dict.items():
    print(f"Вершина {node}: степень {degree}")


# DFS and BFS
print(f"{func.dfs_recursive(G, 'A')} - DFS")
print(f"{func.bfs_recursive(G, deque(["A"]))} - BFS\n")

# dijkstra
# Вычисление кратчайших путей
shortest_distances = dict(func.dijkstra(connections, 'A'))
print("Кратчайшие пути от 'A':")
for vertex, distance in shortest_distances.items():
    print(f"Путь к '{vertex}': {distance}")

# Рисуем граф
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, font_color='black')
plt.title("Граф станций метро")
plt.show()