import streamlit as st
import matplotlib.pyplot as plt
 

def cod_dijkstra():
    st.subheader("Algoritmo de Dijkstra")
    st.markdown(
    """
    El algoritmo de Dijkstra es un algoritmo utilizado en teoría de grafos para encontrar el camino más corto entre un nodo de origen y todos los demás nodos en un grafo dirigido ponderado. Fue propuesto por el científico informático Edsger Dijkstra en 1956 y es ampliamente utilizado en aplicaciones de redes y sistemas de transporte, como enrutadores de red y sistemas de navegación.

El algoritmo de Dijkstra calcula la ruta más corta desde un nodo de origen a todos los demás nodos en un grafo. Toma en cuenta los pesos o costos asociados con las aristas entre los nodos y encuentra la ruta más eficiente en términos de la suma de esos pesos. El algoritmo se basa en un enfoque de "exploración gradual" en el que se expande gradualmente el conjunto de nodos visitados y se actualizan las distancias más cortas a medida que se encuentran rutas más cortas.
    
    """ 
    )
   
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