import networkx as nx

# Crear una instancia de los grafos
graph_min_heap = nx.Graph()
graph_max_heap = nx.Graph()

# Definir una función para agregar nodos al árbol con heap mínimo
def add_node_min_heap(value):
    graph_min_heap.add_node(value)
    if len(graph_min_heap.nodes) > 1:
        parent = (len(graph_min_heap.nodes) - 2) // 2
        graph_min_heap.add_edge(parent, len(graph_min_heap.nodes) - 1)

# Definir una función para agregar nodos al árbol con heap máximo
def add_node_max_heap(value):
    graph_max_heap.add_node(value)
    if len(graph_max_heap.nodes) > 1:
        parent = (len(graph_max_heap.nodes) - 2) // 2
        graph_max_heap.add_edge(parent, len(graph_max_heap.nodes) - 1)