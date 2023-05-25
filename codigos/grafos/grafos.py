import streamlit as st
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from codigos.grafos.rbGraphs import *


def code_grafos():
    st.subheader("Estructura de un Grafo")
    #se vera todo el contenido del codigo en base a grafos
    st.code(
        '''
        class nodoArista(object):
        """Clase nodo vértice"""
            def __init__(self, info, destino):
        """Crea un nodo arista con la intormación cargada."""
                self.info = info
                self.destino = destino
                self.sig = None
        class nodovertice(object):
        """Clase nodo vértice."""
            def __init__(self, info):
        """Crea un nodo vértice con la información cargada."""
                self.info = info
                self.sig - None
                self.visitado = False
                self.adyacentes - Arista()

        class Grafo(object):
        """Clase grafo implementación lista de listas de adyacencia."""
            def __init__(self, dirigido=True):
        """Crea un grafo vacio."""
                self.inicio = None
                self.dirigido = dirigido
                self.tamanio=0
        class Arista(object):
        """Clase lista de arsitas implementación sobre lista."""
            def __init__(self):
        """Crea una lista de aristas vacia."""
                self.inicio = None
                self.tamanio=0

        ''', language='python'
    )
    st.subheader("Eventos")
    opcion = st.selectbox(
        "",
        #Eventos que pueden suceder
        (
            "Insertar_vertices_e_aristas",
            "Agregrar_arista",
            "Eliminar vertice e arista",
            "Buscar vertice o arista",
            "Tamaño", 
            "Existe_paso",
            "Adyacentes",
            "Marcar_no_visitado",
            "Barrido",)
    )

    if opcion == "Insertar_vertices_e_aristas":
        code = '''
        def insertar_vertice(grafo, dato):
"""Inserta un vértice al grafo"""
            nodo = nodoVertice(dato)
            if (grafo. inicio is None or grafo.inicio.info > dato):
                nodo.sig = grafo. inicio
                grafo. inicio = nodo
            else:
                ant = grafo. inicio
                act = grafo. inicio.sig
                while(act is not None and act.info < nodo.info) :
                    ant = act
                    act = act.sig
                nodo.sig = act
                ant.sig = nodo
            grafo. tamanio += 1
            
def insertar_arista(grafo, dato, origen, destino):
"""Inserta una arista desde el vértice origen al destino"""
        agregrar_arista(origen.adyacentes, dato, destino.info)
        if(notgrafo.dirigido):
            agregrar_arista(destino.adyacentes, dato, origen.info)            
            '''

    elif opcion == "Agregrar_arista":
        code = '''
        def agregrar_arista(origen, dato, destino):
"""Agrega la arista desde el vértice origen al destino"""
        nodo = nodoArista(dato, destino)
        if (origen. inicio is None or origen.inicio. destino > destino):
            nodo. sig = origen.inicio
            origen. inicio = nodo
        else:
            ant = origen.inicio
            act = origen.inicio.sig
            while(act is not None and act.destino < nodo.destino):
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        origen. tamanio += 1   
'''
    elif opcion == "Eliminar vertice e arista":
        code = '''
        def eliminar_vertice(grafo, clave):
"""Elimina un vertice del grafo y lo devuelve si lo encuentra."""
    x = None
    if (grafo. inicio.info = clave):
        x= grafo. inicio.info
        grafo. inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo. inicio
        act = grafo.inicio.sig
        while(act is not None and act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            X = act.info
            ant.sig = act.sig
            grafo. tamanio -= 1
    if(x is not None):
        aux = grafo. inicio
        while(aux is not None):
            if(aux.adyacentes.inicio is not None):
                eliminar_arista(aux.adyacentes,clave)
            aux = aux.sig
    return X
    
    
def eliminar_arista(vertice, destino):
"'"'"Elimina una arsita del vertice y lo devuelve si lo encuentra.
    X = None
    if(vertice.inicio.destino=destino):
        x= vertice.inicio.info
        vertice.inicio = vertice.inicio,sig
        vertice. tamanio -= 1
    else:
        ant = vertice. inicio
        act = vertice.inicio,sig
        while(act is not None and act.destino != destino):
            ant = act
            act = act.sig
        if (act is not None):
            X = act. info
            ant.sig = act.sig
            vertice. tamanio -=1

    return X
    
    
    '''
    elif opcion == "Buscar vertice o arista":
        code = '''
       def buscar_vertice(grafo, buscado):
"""Devuelve la direccion del elemento buscado."""
    aux = grafo. inicio
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux


def buscar_arista(vertice, buscado):
"""Devuelve la direccion del elemento buscado."""
    aux=vertice.adyacentes.inicio
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux

    '''
     
    elif opcion == "Tamaño":
        code = '''
           def tamanio(grafo):
"""Devuelve el numero de vertices en el grafo."""
        return grafo, tamanio
'''
    elif opcion == "Existe_paso":
        code = '''
        def existe_paso(grafo, origen, destino):
"""Barrido en profundidad del grafo."""
        resultado = False
        if(not origen. visitado):
            origen. visitado = True
            vadyacentes=origen.adyacentes.inicio
            while(vadyacentes is not None and not resultado) :
                adyacente=buscar_vertice(grafo,vadyacentes.destino)
                if(advacente.info=destino,info):
                    return True
                elif(notadyacente.visitado):
                    resultado = existe_paso(grafo, adyacente, destino)
                adyacentes = vadyacentes.sig
        return resultado

     ''' 
     

    elif opcion == "Adyacentes":
        code = '''
        def adyacentes(vertice):
"""Muestra los adyacents del vertice."""
        aux=vertice.adyacentes.inicio
        while(aux is not None):
            print(aux.destino,aux.info)
            aux = aux.sig


def es_adyacente(vertice, destino):
"""Determina si el destino es advacente directo."""
    resultado = False
    aux=vertice.adyacentes.inicio
    while(aux is not None and not resultado):
        if(aux.destino = resultado):
            resultado = True
        aux = aux.sig
    return resultado
  '''
    elif opcion == "Marcar_no_visitado":
        code = '''
        def marcar_no_visitado(grafo):
"""Marca todos losvertices del grafo como no visitados."""
    aux = grafo.inicio
    while(aux is not None):
        aux. visitado = False
        aux = aux.sig
  '''
    elif opcion == "Barrido":
        code ='''
        def barrido_vertices(grafo):
"""Realiza un barrido de la grafo mostrando sus valores"""
    aux = grafo. inicio
    while(aux is not None):
        print(aux.info)
        aux = aux. sig

def barrido_profundidad(grafo, vertice):
"""Barrido en profundidad del grafo."""
    while(vertice is not None):
        if (not vertice.visitado) :
            vertice. visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while(adyacentes is not None):
                adyacente = buscar _vertice(grafo, adyacentes.destino)
                if(not adyacente. visitado):

def barrido_profundidad(grafo, adyacente)
    adyacentes = adyacentes.sig
    vertice = vertice.sig

def barrido_amplitud(grafo, vertice):
"""Barrido en amplitud del grafo."""
    cola = Cola()
    while(vertice is not None):
        if(not vertice. visitado):
        verticc. visitado = True
        arribo(cola, vertice)
        while(not cola vacia(cola)):
            nodo = atencion(cola)
            print(nodo.info)
            adyacentes-nodo.adyacentes.inicio
            while(adyacentes is not None):
                adyacente = buscar _vertice(grafo, adyacentes.destino)
                if(not adyacente. visitado):
                    adyacente.visitado = True
                    arribo(cola, adyacente)
                adyacentes = adyacentes.sig
    vertice = verlice.sig
  ''' 
    st.code(code, language='python')

def code_dijkstra():
    st.subheader("Estructura del algoritmo de dijkstra")
    st.code(   
        '''
        def dijkstra(grafo, origen, destino):
"""Algoritmo de Dijkstra para hallar el camino mas corto."""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo. inicio
    while(aux is not None):
        if(aux.info = origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no _visitados, [aux, None], inf)
        aux = aux. sig
    while(notheap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar (camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = buscar_h(no_visitados, aux.destino)
            if(no_visitados.vector[pos][o] > dato[0] + aux. info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino
        ''', language='python'
    )
    
    
#----

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
        "1.Grafica del ejerciocio",
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
        "2. Crea una funcion para encontrar el camino mas corto de un grafo",
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
        "2.Grafica del ejerciocio",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
    
        # Crea un grafo de ejemplo
        grafo = nx.Graph()
        grafo.add_edge('A', 'B', weight=3)
        grafo.add_edge('B', 'C', weight=2)
        grafo.add_edge('C', 'D', weight=4)
        grafo.add_edge('A', 'D', weight=5)
    
        # Valores de ejemplo para los nodos iniciales y finales
        nodo_inicial_ejemplo = 'A'
        nodo_final_ejemplo = 'D'

        # Interfaz de Streamlit
        st.title("Encontrar el camino más corto en un grafo")
        nodo_inicial = st.text_input("Ingrese el nodo inicial", value=nodo_inicial_ejemplo)
        nodo_final = st.text_input("Ingrese el nodo final", value=nodo_final_ejemplo)
        if st.button("Encontrar camino más corto"):
            if nodo_inicial and nodo_final:
                # Encuentra el camino más corto utilizando el algoritmo de Dijkstra
                camino = nx.dijkstra_path(grafo, nodo_inicial, nodo_final)
                distancia = nx.dijkstra_path_length(grafo, nodo_inicial, nodo_final)

                # Imprime el camino más corto y la distancia
                st.write("Camino más corto:", camino)
                st.write("Distancia:", distancia)
            else:
                st.write("Ingrese el nodo inicial y el nodo final.")

        # Muestra el grafo
        plt.figure(figsize=(6, 4))
        nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray', linewidths=1)
        plt.title("Grafo")
        plt.axis('off')
        st.pyplot(plt)


def ejercicio3():
    opcion = st.selectbox(
        '3. Crea una funcion que demuestre todos los componentes conectados dentro de un grafo',
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
        "3.Grafica del ejerciocio",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        st.write("Crear Grafo")

        # Obtener la lista de letras ingresadas por el usuario
        letras = st.text_input("Ingrese las letras separadas por espacios").split()

        # Crear un grafo vacío
        G = nx.Graph()

        # Agregar las letras como nodos
        G.add_nodes_from(letras)

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

        # Mostrar los componentes conectados
        st.write("Componentes Conectados:")
        for i, componente in enumerate(componentes_conectados):
            st.write(f"Componente {i+1}: {componente}")

        # Mostrar el grafo
        st.pyplot(plt)


# Ejecutar la función
encontrar_componentes_conectados()
       
        
        
    
        






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

   # Mostrar la matriz de adyacencia resultante
    st.write("Matriz de adyacencia:")
    st.write(matriz)

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
    n = st.number_input("Ingrese el número de nodos del grafo", min_value=1, max_value=10, step=1)
    
    # Solicitar al usuario el tamaño del vector
    n = st.number_input("Ingrese el tamaño del vector", min_value=1, max_value=10, step=1)

  
    vector = []

     # Solicitar al usuario ingresar los elementos del vector
    for i in range(n):
        
        key = f"vector-{i}"
        valor = st.number_input(f"Elemento {i}", key=key)
       
        vector.append(valor)


  
    # Mostrar el vector
    st.write("Vector:")
    st.write(vector)

   
    grafo = nx.Graph()
    grafo.add_nodes_from(range(n))
    # Verificar elementos repetidos en el vector y agregar aristas al grafo
    for i in range(n):
        for j in range(i+1, n):
            if vector[i] == vector[j]:
                grafo.add_edge(i, j)

    # Visualizar el grafo utilizando Matplotlib y NetworkX
    plt.figure(figsize=(6, 4))
    nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray', linewidths=1)
    plt.title("Grafo")
    plt.axis('off')
    st.pyplot(plt)

if __name__ == "__main__":
    in_vector()



def in_matriz():
    st.subheader("Mattriz lista")
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

    # Mostrar la matriz lista
    st.write("Matriz:")
    for row in matriz:
        st.write(row)

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