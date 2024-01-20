import networkx as nx
from collections import deque


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# Граф головних автошляхів України
G = nx.Graph()
G.graph['name'] = 'Ukrain_Roads_Graph'
G.add_nodes_from(['Lviv', 'Kyiv', 'Dnipro', 'Kharkiv', 'Odessa', 'Uman'])
G.add_edges_from([('Lviv', 'Kyiv'), ('Kyiv', 'Kharkiv'), ('Kyiv', 'Dnipro'),
                  ('Kharkiv', 'Dnipro'), ('Dnipro', 'Odessa'), ('Kyiv', 'Uman'),
                  ('Uman', 'Odessa'), ('Uman', 'Lviv'), ('Uman', 'Dnipro') 
                  ])
G['Lviv']['Kyiv']['weight'] = 540
G['Kyiv']['Kharkiv']['weight'] = 481
G['Kyiv']['Dnipro']['weight'] = 453
G['Kharkiv']['Dnipro']['weight'] = 221
G['Dnipro']['Odessa']['weight'] = 480
G['Kyiv']['Uman']['weight'] = 211
G['Uman']['Odessa']['weight'] = 271
G['Uman']['Lviv']['weight'] = 530
G['Uman']['Dnipro']['weight'] = 417


# Запуск рекурсивного алгоритму BFS
print('Aлгоритм BFS (Breadth-first search):')
bfs_recursive(G, deque(['Lviv']))
print()
# Запуск рекурсивного алгоритму DFS
print('Aлгоритм DFS (Depth-first search):')
dfs_recursive(G, 'Lviv')