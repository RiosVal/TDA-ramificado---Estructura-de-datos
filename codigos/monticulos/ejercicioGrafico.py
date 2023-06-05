import streamlit as st
import heapq
from pyvis.network import Network

def heapify(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    return heap

def display_heap(heap):
    net = Network(height="500px", width="700px", notebook=True)
    
    for i in range(len(heap)):
        parent = (i - 1) // 2
        net.add_node(i, label=str(heap[i]), shape="circle", color="lightblue", size=20)
        if parent >= 0:
            net.add_edge(parent, i)
    
    net.barnes_hut(gravity=-8000, central_gravity=0.1, spring_length=100, spring_strength=0.01)
    net.show("heap.html")
    st.components.v1.html(open("heap.html", "r").read(), width=800, height=600)

def ejercicioGrafico():
    st.title("Visualización de Montículos (Heaps)")
    st.write("Un montículo es una estructura de datos de tipo árbol binario completo en la que el valor de cada nodo es menor o igual que sus hijos.")
    st.write("Un montículo se puede representar como una lista en Python. La función `heapify` se utiliza para convertir una lista en un montículo.")
    st.write("La función `display_heap` se utiliza para mostrar gráficamente el montículo en forma de árbol.")

    arr = st.text_input("Ingrese una lista de números separados por comas:")
    if arr:
        arr = [int(num) for num in arr.split(",")]
        heap = heapify(arr)
        display_heap(heap)
