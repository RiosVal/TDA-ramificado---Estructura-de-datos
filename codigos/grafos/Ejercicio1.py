import networkx as nx
import matplotlib.pyplot as plt

def graficar_comunicacion_redes():
    
    redes = ['Red A', 'Red B', 'Red C', 'Red D']

    # Crea un grafo vacío
    grafo = nx.Graph()

    # Agrega los nodos al grafo correspondientes a cada red
    for red in redes:
        grafo.add_node(red)

    # Agrega las aristas al grafo para representar la comunicación entre las redes
    grafo.add_edges_from([('Red A', 'Red B'), ('Red B', 'Red C'), ('Red C', 'Red D'), ('Red D', 'Red A')])

    # Dibuja el grafo
    plt.figure(figsize=(6, 4))
    nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray', linewidths=1)
    plt.title("Comunicación entre redes")
    plt.axis('off')
    plt.show()

  
graficar_comunicacion_redes()