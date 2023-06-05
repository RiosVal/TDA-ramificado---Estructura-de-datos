import streamlit as st
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from codigos.grafos.rbGraphs import *


def ejercicio1():
    opcion = st.selectbox(
        "1. Supongamos que tenemos 4 redes telefonicas ['Red A', 'Red B', 'Red C', 'Red D']  Escribe una función  que demuestre como se comunican las redes",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        code = '''
            class GrafoComunicacion:
        def __init__(self):
        self.nodos = {}
        
    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos[nodo] = {}
            
    def agregar_conexion(self, nodo1, nodo2, peso):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.nodos[nodo1][nodo2] = peso
            self.nodos[nodo2][nodo1] = peso
            
    def obtener_peso_conexion(self, nodo1, nodo2):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            if nodo2 in self.nodos[nodo1]:
                return self.nodos[nodo1][nodo2]
        return None
    
    def obtener_conexiones(self, nodo):
        if nodo in self.nodos:
            return list(self.nodos[nodo].keys())
        return []
    
    def es_conectado(self, nodo1, nodo2):
        return nodo1 in self.nodos and nodo2 in self.nodos[nodo1]
    
    def eliminar_nodo(self, nodo):
        if nodo in self.nodos:
            del self.nodos[nodo]
            for n in self.nodos:
                if nodo in self.nodos[n]:
                    del self.nodos[n][nodo]
'''
        st.code(code, language='python')

def graficar_comunicacion_redes():
    opcion = st.selectbox(
        "1.Grafica del ejercicio",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
    
    
        redes = ['Red A', 'Red B', 'Red C', 'Red D']
    

        # Crea un grafo vacío
        grafo = nx.Graph()

        # Agrega los nodos al grafo correspondientes a cada red
        for red in redes:
            grafo.add_node(red)

        # Muestra el grafo vacío
        plt.figure(figsize=(6, 4))
        plt.title("Comunicación entre redes - Paso 0")
        nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray', linewidths=1)
        plt.axis('off')
        st.pyplot(plt)

        # Agrega las aristas una por una y muestra el grafo actualizado
        for i in range(len(redes)):
            red1 = redes[i]
            red2 = redes[(i + 1) % len(redes)]  # Conecta con la siguiente red en la lista
            grafo.add_edge(red1, red2)

            plt.figure(figsize=(6, 4))
            plt.title(f"Comunicación entre redes - Paso {i+1}")
            nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray', linewidths=1)
            plt.axis('off')
            st.pyplot(plt)

    # Llamada a la función para mostrar el proceso de construcción del grafo
graficar_comunicacion_redes()

    
def ejercicio2():
    opcion = st.selectbox(
        "2.Crea una funcion para encontrar el camino mas corto de un grafo",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        code = '''
        class GrafoComunicacion:
        def __init__(self):
        self.nodos = {}
        
    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos[nodo] = {}
            
    def agregar_conexion(self, nodo1, nodo2, peso):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.nodos[nodo1][nodo2] = peso
            self.nodos[nodo2][nodo1] = peso
            
    def obtener_peso_conexion(self, nodo1, nodo2):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            if nodo2 in self.nodos[nodo1]:
                return self.nodos[nodo1][nodo2]
        return None
    
    def obtener_conexiones(self, nodo):
        if nodo in self.nodos:
            return list(self.nodos[nodo].keys())
        return []
    
    def es_conectado(self, nodo1, nodo2):
        return nodo1 in self.nodos and nodo2 in self.nodos[nodo1]
    
    def eliminar_nodo(self, nodo):
        if nodo in self.nodos:
            del self.nodos[nodo]
            for n in self.nodos:
                if nodo in self.nodos[n]:
                    del self.nodos[n][nodo]'''
        st.code(code, language='python')


def encontrar_camino_mas_corto():
    opcion = st.selectbox(
        "2.Gráfica del ejercicio",
        ("-", "Mostrar solución")
    )
    grafo = nx.Graph()
    grafo.add_edge('A', 'B', weight=3)
    grafo.add_edge('B', 'C', weight=2)
    grafo.add_edge('C', 'D', weight=4)
    grafo.add_edge('A', 'D', weight=5)
    pos = nx.spring_layout(grafo)  # Calcula la disposición de los nodos

    if opcion == "Mostrar solución":
        # Valores de ejemplo para los nodos iniciales y finales
        nodo_inicial_ejemplo = 'A'
        nodo_final_ejemplo = 'D'

        # Interfaz de Streamlit
        st.title("Encontrar el camino más corto en un grafo")
        nodo_inicial = st.text_input("Ingrese el nodo inicial", value=nodo_inicial_ejemplo)
        nodo_final = st.text_input("Ingrese el nodo final", value=nodo_final_ejemplo)

        if st.button("Mostrar grafo y solución"):
            # Encuentra el camino más corto utilizando el algoritmo de Dijkstra
            camino = nx.dijkstra_path(grafo, nodo_inicial, nodo_final)
            distancia = nx.dijkstra_path_length(grafo, nodo_inicial, nodo_final)

            # Dibuja el grafo inicial
            plt.figure(figsize=(10, 5))
            plt.subplot(1, 2, 1)
            nx.draw(grafo, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray', linewidths=1)
            plt.title("Grafo inicial")
            plt.axis('off')

            # Dibuja el grafo con el camino más corto resaltado
            plt.subplot(1, 2, 2)
            node_colors = ['lightblue' if nodo in camino else 'gray' for nodo in grafo.nodes]
            edge_colors = ['red' if (nodo1, nodo2) in zip(camino, camino[1:]) else 'gray' for nodo1, nodo2 in grafo.edges]
            nx.draw(grafo, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10, edge_color=edge_colors, linewidths=1)
            plt.title("Grafo con camino más corto resaltado")
            plt.axis('off')

            st.pyplot(plt)

encontrar_camino_mas_corto()


def ejercicio3():
    opcion = st.selectbox(
        '3.Crea una funcion que demuestre todos los componentes conectados dentro de un grafo',
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        code = '''
            from collections import deque

class GrafoComunicacion:
    def __init__(self):
        self.grafo = {}
        
    def agregar_nodo(self, nodo):
        self.grafo[nodo] = []
        
    def agregar_conexion(self, nodo1, nodo2):
        self.grafo[nodo1].append(nodo2)
        self.grafo[nodo2].append(nodo1)
        
    def obtener_conexiones(self, nodo):
        return self.grafo[nodo]
        
    def componentes_conectados(self):
        visitados = set()
        componentes = []
        for nodo in self.grafo:
            if nodo not in visitados:
                componente = set()
                cola = deque([nodo])
                while cola:
                    nodo_actual = cola.popleft()
                    componente.add(nodo_actual)
                    visitados.add(nodo_actual)
                    for nodo_conectado in self.grafo[nodo_actual]:
                        if nodo_conectado not in visitados:
                            cola.append(nodo_conectado)
                componentes.append(componente)
        return componentes
'''
        st.code(code, language='python')


def encontrar_componentes_conectados():
    opcion = st.selectbox(
        "3.Grafica del ejercicio",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        st.write("Crear Grafo")

        # Obtener la lista de letras ingresadas por el usuario
        letras_1 = st.text_input("Ingrese las letras separadas por espacios :)").split()

        # Crear un grafo vacío
        G = nx.Graph()

        # Agregar las letras como nodos
        G.add_nodes_from(letras_1)

        st.write("Conexiones")

        # Obtener las conexiones ingresadas por el usuario
        conexiones = st.text_input("Ingrese las conexiones en el formato A-B, separadas por espacios").split()

        # Agregar las conexiones al grafo
        for conexion in conexiones:
            nodo1, nodo2 = conexion.split('-')
            G.add_edge(nodo1, nodo2)

        # Encontrar los componentes conectados
        componentes_conectados = nx.connected_components(G)

        # Dibujar el grafo
        plt.figure(figsize=(6, 6))
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=12, edge_color='gray', width=2)

       
       

        # Mostrar el grafo
        st.pyplot(plt)
# Ejecutar la función
encontrar_componentes_conectados()


def servicio():
    opcion = st.selectbox(
        "Mostrar gráfico",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        # Crear el grafo vacío
        G = nx.Graph()

        # Agregar el nodo de servicio técnico
        G.add_node("Empresa")

        # Obtener la lista de letras ingresadas por el usuario
        letras = st.text_input("Ingrese las letras separadas por espacios").split()

        # Crear un heap de prioridad para almacenar las aristas
        heap = []

        # Agregar las aristas al heap
        for letra in letras:
            distancia = st.number_input(f"Ingrese la distancia desde 'serviciotécnico' hasta '{letra}'", value=0.0, min_value=0.0)
            heapq.heappush(heap, (distancia, letra))

        # Verificar si se ingresaron aristas
        if heap:
            # Encontrar la arista más corta
            distancia_minima, nodo_siguiente = heapq.heappop(heap)

            # Agregar la arista más corta al grafo
            G.add_edge("Empresa", nodo_siguiente)

            # Actualizar el nodo actual
            nodo_actual = nodo_siguiente

            # Guardar el primer nodo encontrado
            primeroN = nodo_actual

            # Lista para almacenar los nodos recorridos
            nodos_recorridos = ["Empresa", nodo_actual]

            # Buscar otras aristas con la misma distancia mínima desde 'serviciotécnico'
            while heap and heap[0][0] == distancia_minima:
                _, nodo_siguiente = heapq.heappop(heap)
                G.add_edge("Empresa", nodo_siguiente)
                nodos_recorridos.append(nodo_siguiente)

            # Continuar buscando la siguiente arista más corta desde los nodos actuales
            while heap:
                # Reiniciar el heap para la búsqueda desde los nodos actuales
                heapq.heapify(heap)

                # Encontrar la siguiente arista más corta desde el nodo actual
                distancia_minima, nodo_siguiente = heapq.heappop(heap)
                G.add_edge(nodo_actual, nodo_siguiente)
                nodos_recorridos.append(nodo_siguiente)

                # Actualizar el nodo actual
                nodo_actual = nodo_siguiente

            # Mostrar los nodos recorridos
            st.write("La ruta que debe recorrer es..")
            for i, nodo in enumerate(nodos_recorridos):
                st.write(f"{i+1}. {nodo}")

            # Dibujar el grafo (si se seleccionó la opción correspondiente)
            if opcion == "Mostrar solución":
                plt.figure(figsize=(6, 6))
                pos = nx.spring_layout(G)
                nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=12, edge_color='gray', width=2)
                st.pyplot(plt)

        else:
            st.write("No se ingresaron aristas")

# Ejecutar la función
servicio()