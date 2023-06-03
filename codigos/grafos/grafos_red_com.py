import streamlit as st
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from codigos.grafos.rbGraphs import *
import heapq

def servicio():
    # Crear el grafo con los nodos y aristas
    graph = {
        'serviciotécnico': {'A': 0, 'B': 0, 'C': 0},  # Aristas desde el nodo 'serviciotécnico' con distancia 0
        'A': {'B': 0, 'C': 0},
        'B': {'A': 0, 'C': 0},
        'C': {'A': 0, 'B': 0}
    }

    # Inicializar distancias con infinito excepto para el nodo 'serviciotécnico'
    distances = {node: float('inf') for node in graph}
    distances['serviciotécnico'] = 0

    # Cola de prioridad para almacenar los nodos a visitar
    pq = [(0, 'serviciotécnico')]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, distance in graph[current_node].items():
            new_distance = current_distance + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    # Mostrar las distancias más cortas desde 'serviciotécnico' a los demás nodos
    for node, distance in distances.items():
        print(f"Distancia desde 'serviciotécnico' a '{node}': {distance}")

# Ejecutar la función
servicio()

