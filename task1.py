import networkx as nx
import matplotlib.pyplot as plt

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


print(f'Кількість верщин графу: {G.number_of_nodes()}, кількість ребер: {G.number_of_edges()}')
print(f'Ступінь центральності (Degree Centrality): {nx.degree_centrality(G)}')
print(f'Близькість вузла (Closeness Centrality): {nx.closeness_centrality(G)}')
print(f'Посередництво вузла (Betweenness Centrality): {nx.betweenness_centrality(G)}')

plt.figure(figsize=(14,8))
labels = nx.get_edge_attributes(G, 'weight')
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, font_size=16, node_size=4000, node_color='yellow')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()