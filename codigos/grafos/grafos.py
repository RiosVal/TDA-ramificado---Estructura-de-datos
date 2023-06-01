import streamlit as st
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
