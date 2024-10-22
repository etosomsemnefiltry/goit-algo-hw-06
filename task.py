import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import func

G = nx.Graph()

# Строим метро
stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(stations)

# Связи между станциями
connections = [('A', 'B'), ('A', 'C'), ('B', 'D'), 
               ('B', 'D'), ('D', 'F'), ('G', 'D'),
               ('C', 'D'), ('D', 'E'), ('E', 'F'), 
               ('F', 'G'), ('F', 'H'), ('G', 'H')]
G.add_edges_from(connections)

G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=10)
G.add_edge('B', 'D', weight=3)
G.add_edge('B', 'D', weight=8)  
G.add_edge('D', 'F', weight=6)
G.add_edge('G', 'D', weight=12)
G.add_edge('C', 'D', weight=2)
G.add_edge('D', 'E', weight=4)
G.add_edge('E', 'F', weight=9)
G.add_edge('F', 'G', weight=7)
G.add_edge('F', 'H', weight=11)
G.add_edge('G', 'H', weight=1)

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
shortest_paths = dict(nx.single_source_dijkstra_path(G, 'A'))
shortest_distances = dict(nx.single_source_dijkstra_path_length(G, 'A'))
print("Кратчайшие пути от 'A':")
for destination, path in shortest_paths.items():
    print(f"К ' {destination}': путь {path}, расстояние {shortest_distances[destination]}")

# Рисуем граф
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, font_color='black')
plt.title("Граф станций метро")
plt.show()