import streamlit as st
from codigos.monticulos.heap import *
import heapq

def ejercicio1():

    opcion = st.selectbox(
        "1. En una matrix implementa operaciones de inserccion, eliminacion y una operacion para obtener el maximo",
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
    st.subheader("Aplicación de monticulos (HEAP)")
    st.write("<h5>Explicación:</h5>",unsafe_allow_html=True)
    st.write("""
        - Para encontrar los elementos más grandes, se utiliza la función nlargest(k, numbers), donde k es el número de elementos más grandes que el usuario desea obtener, y numbers es la lista de números ingresados por el usuario. Esta función devuelve una lista con los k elementos más grandes del heap. 
        - Para encontrar los elementos más pequeños, se utiliza la función nsmallest(k, numbers), de manera similar a la función nlargest(). Esta función devuelve una lista con los k elementos más pequeños del heap.
        - El ordenamiento de los elementos en un heap se basa en la propiedad de heap, que establece que para cada nodo del heap, el valor del nodo padre es mayor o menor que los valores de sus nodos hijos, dependiendo de si es un max heap o un min heap, respectivamente.
        - El siguiente ejemplo, utiliza la función heapify() de la biblioteca heapq para construir el heap a partir de la lista de números ingresados por el usuario. La función heapify() realiza el proceso de ordenamiento del heap, reorganizando los elementos de la lista para que cumplan con la propiedad de heap.
        """)


    # Inicializar una lista vacía para almacenar los números ingresados por el usuario
    numbers = []

    # Obtener la entrada del usuario
    user_input = st.text_input("Ingrese una lista de números separados por comas")

    # Convertir la entrada del usuario en una lista de números
    if user_input:
        numbers = [int(num.strip()) for num in user_input.split(',')]

    # Mostrar los números ingresados
    st.write("Números ingresados:", numbers)

    if numbers:
        # Construir un heap a partir de los números ingresados
        heapq.heapify(numbers)

        # Obtener la opción del usuario (mayor o menor)
        option = st.selectbox("Seleccione una opción", ["Mayor", "Menor"])

        if option == "Mayor":
            # Obtener los k elementos más grandes del heap
            k = st.number_input("Ingrese el número de elementos más grandes", min_value=1, max_value=len(numbers),
                                value=1, step=1)
            largest = heapq.nlargest(k, numbers)
            st.write(f"{k} elementos más grandes:", largest)
        elif option == "Menor":
            # Obtener los k elementos más pequeños del heap
            k = st.number_input("Ingrese el número de elementos más pequeños", min_value=1, max_value=len(numbers),
                                value=1, step=1)
            smallest = heapq.nsmallest(k, numbers)
            st.write(f"{k} elementos más pequeños:", smallest)


def ejercicio3():
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
    