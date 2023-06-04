import streamlit as st
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from codigos.grafos.rbGraphs import *

def in_adya():
    st.subheader("Matriz adyacencia")
    st.markdown(
    """
    La matriz de adyacencia es una representación de un grafo mediante una matriz cuadrada. En esta matriz, las filas y columnas representan los vértices del grafo, y los elementos de la matriz indican si hay una arista o conexión entre los vértices correspondientes
    
    """ 
    )
    # Solicitar al usuario el número de nodos del grafo
    n = st.number_input("Ingrese el número de nodos del grafo", min_value=1, max_value=10, step=1)

    # Crear una matriz de ceros de tamaño n x n utilizando NumPy    
    matriz = np.zeros((n, n))

    # Solicitar al usuario ingresar los elementos de la matriz de adyacencia
    for i in range(n):
        for j in range(n):
            
            key = f"matriz-{i}-{j}"
            valor = st.number_input(f"Elemento ({i}, {j})", key=key)
            
            matriz[i, j] = valor


    # Crear un grafo a partir de la matriz de adyacencia utilizando NetworkX 
    grafo = nx.from_numpy_array(matriz)

    # Visualizar el grafo utilizando Matplotlib y NetworkX
    plt.figure(figsize=(6, 4))
    nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray', linewidths=1)
    plt.title("Grafo")
    plt.axis('off')
    st.pyplot(plt)

if __name__ == "__main__":
    in_adya()


def in_vec():
    st.subheader("Matriz vector")
    st.markdown(
        """
        La matriz de un vector es una estructura rectangular compuesta por una sola columna o una sola fila de elementos. Esta matriz se utiliza para almacenar y manipular un conjunto de valores ordenados de forma lineal.
        """
    )
    # Solicitar al usuario el tamaño del vector
    n = st.number_input("Ingrese el número de nodos del grafo", min_value=1, max_value=10, step=1, key="numero_nodos")

    vector = []

    # Solicitar al usuario ingresar los elementos del vector
    for i in range(n):
        key = f"vector-{i}"
        valor = st.number_input(f"Elemento {i}", key=key)
        vector.append(valor)

    grafo = nx.Graph()
    grafo.add_nodes_from(range(n))
    # Verificar elementos repetidos en el vector y agregar aristas al grafo
    for i in range(n):
        for j in range(i + 1, n):
            if vector[i] == vector[j]:
                grafo.add_edge(i, j)

    # Verificar si el grafo tiene aristas
    if grafo.number_of_edges() == 0:
        st.write("No se encontraron aristas en el grafo. Verifique los elementos ingresados.")

    # Visualizar el grafo utilizando Matplotlib y NetworkX
    pos = nx.spring_layout(grafo)  # Layout del grafo
    plt.figure(figsize=(6, 4))
    nx.draw(
        grafo,
        pos=pos,
        with_labels=True,
        node_color="lightblue",
        node_size=500,
        font_size=10,
        edge_color="gray",
        linewidths=1,
    )
    plt.title("Grafo")
    plt.axis("off")
    st.pyplot(plt)


if __name__ == "__main__":
    in_vec()



def in_matriz():
    st.subheader("Matriz lista")
    st.markdown(
    """
   La matriz de lista es una representación de un grafo mediante una estructura de datos que utiliza listas en lugar de una matriz cuadrada. En esta representación, cada vértice del grafo se mapea a una lista que contiene los vértices adyacentes a él. Cada elemento de la lista representa una conexión o arista entre los vértices. Esta representación es eficiente para grafos dispersos, ya que solo se almacenan las conexiones existentes y no se desperdicia espacio para conexiones ausentes. 
    
    """ 
    
    )
    # Solicitar al usuario el tamaño de la matriz
    n = st.number_input("Ingrese el tamaño de la matriz", min_value=1, max_value=10, step=1)

   # Crear una matriz lista vacía
    matriz = [[] for _ in range(n)]

   
    # Solicitar al usuario ingresar los elementos de la matriz lista
    for i in range(n):
        for j in range(n):
         
            valor = st.number_input(f"Elemento ({i}, {j})")
   
            matriz[i].append(valor)

    


    # Crear un grafo vacío
    grafo = nx.Graph()
    grafo.add_nodes_from(range(n))
    # Visualizar el grafo utilizando Matplotlib y NetworkX
    for i in range(n):
        for j in matriz[i]:
            if j != 0:
                grafo.add_edge(i, j)


    plt.figure(figsize=(6, 4))
    nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray', linewidths=1)
    plt.title("Grafo")
    plt.axis('off')
    st.pyplot(plt)

if __name__ == "__main__":
    in_matriz()
