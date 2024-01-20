def print_table(distances):
    # Верхній рядок таблиці
    print("{:<10} {:<10}".format("Вершина", "Відстань"))
    print("-" * 20)
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        print("{:<10} {:<10}".format(vertex, distance))

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
    return distances


# Граф головних автошляхів України
graph = {
    'Lviv': {'Kyiv': 540, 'Uman': 530},
    'Kyiv': {'Lviv': 540, 'Uman': 211, 'Dnipro': 453, 'Kharkiv': 481},
    'Uman': {'Lviv': 530, 'Kyiv': 211, 'Dnipro': 417, 'Odessa': 271},
    'Kharkiv': {'Kyiv': 481, 'Dnipro': 221},
    'Dnipro': {'Odessa': 480, 'Uman': 417, 'Kyiv': 453, 'Kharkiv': 221},
    'Odessa': {'Dnipro': 480, 'Uman': 271}
}

for vertex in graph.keys():
    print(f'\nНайменша відстань між вершиною {vertex} та іншими:')
    print_table(dijkstra(graph, vertex))