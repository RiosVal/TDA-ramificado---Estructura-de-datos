import streamlit as st
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from codigos.grafos.rbGraphs import *

def code_atender_servicio():
    st.subheader("Actividad")
    opcion = st.selectbox(
        "Se tiene un sistema de redes conectados con varios puntos de una ciudad; un trabajador hace mantenimientos a este sistema de redes y tiene que ir por todas las conexiones del sistema(nodos). Para encontrar el trayecto mas optimo se realiza un grafo teniendo en cuenta la distancia de cada nodo.",
        ("-", "Mostrar solución")
    )
    
    

    
    if opcion == "Mostrar solución":
        code = '''def calcular_distancia(cliente1, cliente2):
    # Aquí puedes implementar tu lógica para calcular la distancia entre dos clientes
    # Puedes utilizar cualquier algoritmo o fórmula que sea adecuada para tu caso
    # En este ejemplo, simplemente se retorna la diferencia entre los números de cliente
    return abs(cliente1 - cliente2)

def atender_servicio():
    # Preguntar al empleado cuántos clientes son
    n_clientes = int(input("¿Cuántos clientes son? "))

    # Crear una lista para almacenar las distancias con cada cliente
    distancias = []

    # Preguntar al empleado la distancia con cada cliente
    for i in range(n_clientes):
        distancia = float(input(f"¿Cuál es la distancia con el cliente {i+1}? "))
        distancias.append(distancia)

    # Preguntar al empleado con qué cliente inicia el servicio
    cliente_inicial = int(input("¿Con qué cliente desea iniciar el servicio? "))

    # Validar que el número de cliente inicial sea válido
    if cliente_inicial < 1 or cliente_inicial > n_clientes:
        print("El número de cliente inicial no es válido.")
        return

    # Iniciar el servicio atendiendo a todos los clientes
    clientes_atendidos = [cliente_inicial]
    while len(clientes_atendidos) < n_clientes:
        cliente_actual = clientes_atendidos[-1]  # Último cliente atendido
        distancia_minima = float('inf')
        cliente_siguiente = -1

        # Encontrar el siguiente cliente más cercano que no haya sido atendido
        for i in range(n_clientes):
            if (i+1) not in clientes_atendidos:
                distancia = calcular_distancia(cliente_actual, i+1)
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    cliente_siguiente = i+1

        clientes_atendidos.append(cliente_siguiente)

    # Mostrar el orden en el que se atendieron los clientes
    print("El orden de atención de los clientes es:")'''

        st.code(code, language='python')



