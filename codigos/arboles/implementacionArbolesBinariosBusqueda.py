from codigos.arboles.arbolesBinariosBusqueda import *
import streamlit as st

def insertar_nodos() -> ArbolBinario:
    arbol = ArbolBinario()
    # Verifica si la lista ya existe en el estado de la sesión
    if 'lista_nodos' not in st.session_state:
        st.session_state.lista_nodos = []  # Crea una lista vacía en el estado de la sesión

    # Crea un campo de entrada numérica
    numero = st.number_input('Ingresa el valor del nodo')

    # Agrega el número ingresado a la lista cuando se hace clic en el botón
    if st.button("Insertar"):
        st.session_state.lista_nodos.append(numero)
    for numero in st.session_state.lista_nodos:
        arbol.insertar(numero)
    
    return arbol

def buscar_eliminar_nodo(arbol: ArbolBinario):
    eliminados, buscados = st.columns(2)
    with eliminados:
        num_eliminar = st.number_input('Número a eliminar')
        if st.button('Eliminar'):
            arbol.eliminar(num_eliminar)
    with buscados:
        num_buscado = st.number_input('Número a buscar')
        if st.button('Buscar'):
            buscado = arbol.buscar(num_buscado)
            if buscado == True:
                st.write('El número se encuentra en el árbol')
            else:
                st.write('El número no se encuentra en el árbol')
