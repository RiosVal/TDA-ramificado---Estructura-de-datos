import streamlit as st
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from codigos.grafos.rbGraphs import *


def in_adya():
    st.subheader("Matriz de adyacencia")
    st.markdown(
        """
        La matriz de adyacencia es una representación de un grafo mediante una matriz cuadrada. En esta matriz, las filas y columnas representan los vértices del grafo, y los elementos de la matriz indican si hay una arista o conexión entre los vértices correspondientes.
        """
    )

    # Solicitar al usuario los nombres de los nodos separados por espacios
    nodos_input = st.text_input("Ingrese los nombres de los nodos separados por espacios")
    nodos = nodos_input.split()

    # Obtener el número de nodos del grafo
    n = len(nodos)

    # Crear una matriz de ceros de tamaño n x n utilizando NumPy    
    matriz = np.zeros((n, n))

    # Solicitar al usuario ingresar los elementos de la matriz de adyacencia
    for i in range(n):
        for j in range(n):
            key = f"matriz-{i}-{j}"
            valor = st.number_input(f"Ingrese el valor del nodo ({nodos[i]}, {nodos[j]})", key=key)
            matriz[i, j] = valor

    # Mostrar botón para graficar el grafo
    if st.button("Mostrar grafo"):
        # Crear un grafo a partir de la matriz de adyacencia utilizando NetworkX 
        grafo = nx.from_numpy_array(matriz)

        # Asignar los nombres de los nodos al grafo
        mapeo_nodos = {i: nodo for i, nodo in enumerate(nodos)}
        grafo = nx.relabel_nodes(grafo, mapeo_nodos)

        # Visualizar el grafo utilizando Matplotlib y NetworkX
        plt.figure(figsize=(6, 4))
        nx.draw(
            grafo,
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
    in_adya()






def in_vec():
    st.subheader("Matriz vector")
    st.markdown(
        """
        La matriz de un vector es una estructura rectangular compuesta por una sola columna o una sola fila de elementos. Esta matriz se utiliza para almacenar y manipular un conjunto de valores ordenados de forma lineal.
        """
    )
    
    # Solicitar al usuario los nombres de los nodos separados por espacios
    nodos_input = st.text_input("Ingrese los nombres de los nodos separados por espacios", key="nodos_input")
    nodos = nodos_input.split()

    # Obtener el número de nodos del grafo
    n = len(nodos)

    vector = []

    # Solicitar al usuario ingresar los valores de los nodos
    for i in range(n):
        key = f"vector-{i}"
        valor = st.number_input(f"Ingrese el valor del nodo {nodos[i]}", key=key)
        vector.append(valor)

    # Crear un grafo vacío
    grafo = nx.Graph()

    # Agregar los nodos al grafo
    grafo.add_nodes_from(nodos)

    # Verificar elementos repetidos en el vector y agregar aristas al grafo
    for i in range(n):
        for j in range(i + 1, n):
            if vector[i] == vector[j]:
                grafo.add_edge(nodos[i], nodos[j])

    # Verificar si el grafo tiene aristas
    if grafo.number_of_edges() == 0:
        st.write("No se encontraron aristas en el grafo. Verifique los elementos ingresados.")

    # Mostrar botón para graficar el grafo
    button_key = "mostrar_grafo"
    if st.button("Mostrar grafo", key=button_key):
        # Visualizar el grafo utilizando Matplotlib y NetworkX
        plt.figure(figsize=(6, 4))
        nx.draw(
            grafo,
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


import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def in_matriz():
    st.subheader("Matriz lista")
    st.markdown(
        """
        La matriz lista es una representación de un grafo mediante una estructura de datos que utiliza listas en lugar de una matriz cuadrada. En esta representación, cada vértice del grafo se mapea a una lista que contiene los vértices adyacentes a él. Cada elemento de la lista representa una conexión o arista entre los vértices. Esta representación es eficiente para grafos dispersos, ya que solo se almacenan las conexiones existentes y no se desperdicia espacio para conexiones ausentes.
        """
    )

    # Solicitar al usuario los nombres de los nodos separados por espacios
    nodos_input = st.text_input("Ingrese los nombres de los nodos separados por espacios", key="nodos_input_unique")
    nodos = nodos_input.split()

    # Obtener el número de nodos del grafo
    n = len(nodos)

    # Crear una matriz lista vacía
    matriz = [[] for _ in range(n)]

    # Solicitar al usuario ingresar los elementos de la matriz lista
    for i in range(n):
        for j in range(n):
            valor = st.number_input(f"Ingrese el valor del nodo ({nodos[i]}, {nodos[j]})", key=f"valor-{i}-{j}")
            matriz[i].append(valor)

    # Mostrar botón para graficar el grafo
    if st.button("Mostrar grafo", key="mostrar-grafo"):
        # Crear un grafo vacío
        grafo = nx.Graph()
        grafo.add_nodes_from(nodos)

        # Agregar aristas al grafo basado en la matriz lista
        for i in range(n):
            for j in range(n):
                if matriz[i][j] != 0:
                    grafo.add_edge(nodos[i], nodos[j])

        # Visualizar el grafo utilizando Matplotlib y NetworkX
        plt.figure(figsize=(6, 4))
        nx.draw(
            grafo,
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
    in_matriz()



