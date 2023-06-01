from codigos.arboles.TDAarbolBinario import BinaryTree
import streamlit as st

def insertar_nodos() -> BinaryTree:
    """Permite al usuario insertar nodos en un árbol binario interactivo

    Returns:
        ArbolBinario: arbol binario creado
    """
    arbol = BinaryTree()
    # Verifica si la lista ya existe en el estado de la sesión
    if 'lista_nodos' not in st.session_state:
        st.session_state.lista_nodos = []  # Crea una lista vacía en el estado de la sesión

    # Crea un campo de entrada numérica
    numero = st.number_input('Ingresa el valor del nodo')

    # Agrega el número ingresado a la lista cuando se hace clic en el botón
    if st.button("Insertar"):
        st.session_state.lista_nodos.append(numero)
    for numero in st.session_state.lista_nodos:
        arbol.add(numero)
    
    return arbol

def buscar_eliminar_nodo(arbol: BinaryTree):
    """Permite al usuario buscar y eliminar nodos en el árbol binario

    Args:
        arbol (ArbolBinario): árbol en donde se ejecutarán las acciones
    """
    eliminados, buscados = st.columns(2)
    with eliminados:
        num_eliminar = st.number_input('Número a eliminar')
        if st.button('Eliminar'):
            arbol.delete(num_eliminar)
    with buscados:
        num_buscado = st.number_input('Número a buscar')
        if st.button('Buscar'):
            buscado = arbol.search(num_buscado)
            if buscado != None:
                st.write('El número se encuentra en el árbol')
            else:
                st.write('El número no se encuentra en el árbol')
