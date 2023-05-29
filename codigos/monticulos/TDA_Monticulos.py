import streamlit as st

class TdaMonticulo:
    def __init__(self, tamaño):
        self.heap = [None] * tamaño
        self.size = 0

    def agregar(self, dato):
        if self.size >= len(self.heap):
            # El montículo está lleno
            return
        self.heap[self.size] = dato
        self.flotar(self.size)
        self.size += 1

    def quitar(self):
        if self.size == 0:
            # El montículo está vacío
            return None
        dato = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.hundir(0)
        return dato

    def flotar(self, índice):
        padre = (índice - 1) // 2
        while índice > 0 and self.heap[índice] > self.heap[padre]:
            self.heap[índice], self.heap[padre] = self.heap[padre], self.heap[índice]
            índice = padre
            padre = (índice - 1) // 2

    def hundir(self, índice):
        hijo_izquierdo = 2 * índice + 1
        hijo_derecho = 2 * índice + 2
        índice_mayor = índice

        if hijo_izquierdo < self.size and self.heap[hijo_izquierdo] > self.heap[índice_mayor]:
            índice_mayor = hijo_izquierdo
        if hijo_derecho < self.size and self.heap[hijo_derecho] > self.heap[índice_mayor]:
            índice_mayor = hijo_derecho

        if índice_mayor != índice:
            self.heap[índice], self.heap[índice_mayor] = self.heap[índice_mayor], self.heap[índice]
            self.hundir(índice_mayor)

    def montículo_vacio(self):
        return self.size == 0

    def montículo_lleno(self):
        return self.size == len(self.heap)

    def tamaño(self):
        return self.size

    @classmethod
    def monticulizar(cls, elementos):
        tamaño = len(elementos)
        monticulo = cls(tamaño)
        monticulo.heap = elementos
        monticulo.size = tamaño

        for i in range(tamaño // 2 - 1, -1, -1):
            monticulo.hundir(i)

        return monticulo
    
    def imprimir_heap(self): #Imprimir monticulo
        print(self.heap[:self.size])

    def imprimir_heap_streamlit(self):#Imprimir monticulo compatible con STREAMLIS
        heap = self.heap[:self.size]

        st.write("Elementos del montículo:")
        for i, avion in heap:
            st.write(f"{i})  Tipo: {avion[1]}   -   Prioridad: {avion[0]}")