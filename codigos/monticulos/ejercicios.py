import streamlit as st
import heapq

def ejercicio1():

    opcion = st.selectbox(
        "1.En una matrix implementa operaciones de inserccion, eliminacion y una operacion para obtener el maximo",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        code = '''
        class Monticulo:
        def __init__(self):
            self.heap = []
        
        def insert(self, value):
            self.heap.append(value)
            self._sift_up(len(self.heap) - 1)
        
        def delete(self):
            if not self.heap:
                return None
            self._swap(0, len(self.heap) - 1)
            max_value = self.heap.pop()
            self._sift_down(0)
            return max_value
        
        def get_max(self):
            if not self.heap:
                return None
            return self.heap[0]
        
        def _sift_up(self, index):
            parent = (index - 1) // 2
            if parent >= 0 and self.heap[parent] < self.heap[index]:
                self._swap(parent, index)
                self._sift_up(parent)
        
        def _sift_down(self, index):
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index
            
            if (
                left_child < len(self.heap) and
                self.heap[left_child] > self.heap[largest]
            ):
                largest = left_child
            
            if (
                right_child < len(self.heap) and
                self.heap[right_child] > self.heap[largest]
            ):
                largest = right_child
            
            if largest != index:
                self._swap(index, largest)
                self._sift_down(largest)
        
        def _swap(self, i, j):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    # Ejemplo de uso
    monticulo = Monticulo()
    monticulo.insert(5)
    monticulo.insert(10)
    monticulo.insert(3)
    print(monticulo.get_max())  # Debe imprimir 10
    print(monticulo.delete())   # Debe imprimir 10
    print(monticulo.get_max())  # Debe imprimir 5

    '''
        st.code(code, language='python')

def ejercicio2():
    opcion = st.selectbox(
       '2.Calcular el enesimo de una secuencia Fibonacci',
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        code = '''
         def fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    
    return b

# Ejemplo de uso
print(fibonacci(1))   # Debe devolver 0
print(fibonacci(5))   # Debe devolver 3
print(fibonacci(10))  # Debe devolver 34


'''
        st.code(code, language='python')
    