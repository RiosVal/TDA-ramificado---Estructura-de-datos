import streamlit as st
from codigos.monticulos.heap import *
import heapq
import io
import matplotlib.pyplot as plt

def ejercicio1():

    opcion = st.selectbox(
        "1. Cree una cola de monticulo utilizando el módulo heapq en Python y realiza varias operaciones, como convertir una lista en un montón, agregar un nuevo valor al montón, eliminar el elemento más pequeño del montón, obtener los n elementos más pequeños y los n más grandes de el montón",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        code = '''
                import heapq

        # Initialize a list with some values
        values = [5, 1, 3, 7, 4, 2]

        # Convert the list into a heap
        heapq.heapify(values)

        # Print the heap
        print("Heap:", values)

        # Add a new value to the heap
        heapq.heappush(values, 6)

        # Print the updated heap
        print("Heap after push:", values)

        # Remove and return the smallest element from the heap
        smallest = heapq.heappop(values)

        # Print the smallest element and the updated heap
        print("Smallest element:", smallest)
        print("Heap after pop:", values)

        # Get the n smallest elements from the heap
        n_smallest = heapq.nsmallest(3, values)

        # Print the n smallest elements
        print("Smallest 3 elements:", n_smallest)

        # Get the n largest elements from the heap
        n_largest = heapq.nlargest(2, values)

        # Print the n largest elements
        print("Largest 2 elements:", n_largest)

    '''
        st.code(code, language='python')
    

    st.write( "<h4>Ejemplo de Ejercicio 1</h4>",unsafe_allow_html=True )

    numeros = []

    inputuser = st.text_input("Ingresa una lista de numeros separados por comas ( , )")

    if inputuser:
        numeros = [int(num.strip()) for num in inputuser.split(',')]

        # Mostrar los números ingresados
        st.write("Números ingresados:", numeros)

    if numeros:
        # Construir un heap a partir de los números ingresados
        heapq.heapify(numeros)

        maspequeño = heapq.heappop(numeros)

        st.write("El numero mas pequeño es:", maspequeño)

        st.write("Monticulo despues del pop", numeros)

        p = st.number_input("Ingrese el número de elementos más pequeños", min_value=1, max_value=len(numeros),
                                value=1, step=1)
        
        N_pequeños = heapq.nsmallest(p, numeros)

        st.write(f"{p} elementos mas pequeños:", N_pequeños)

        g = st.number_input("Ingrese el número de elementos más grandes", min_value=1, max_value=len(numeros),
                                value=1, step=1)
        
        N_grande = heapq.nlargest(g, numeros)

        st.write(f"{g} elementos más grandes:", N_grande)

         # Crear el grafo
        G = nx.DiGraph()

        # Agregar nodos para los números ingresados
        for i, num in enumerate(numeros):
            G.add_node(num)

        # Agregar aristas para las relaciones del montículo
        for i, num in enumerate(numeros):
            if 2 * i + 1 < len(numeros):
                G.add_edge(num, numeros[2 * i + 1])
            if 2 * i + 2 < len(numeros):
                G.add_edge(num, numeros[2 * i + 2])

        # Dibujar el grafo
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10)
        plt.title('Montículo')
        plt.axis('off')
        st.pyplot(plt)


   
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
