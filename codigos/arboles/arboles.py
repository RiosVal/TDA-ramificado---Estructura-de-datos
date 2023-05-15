import streamlit as st
from codigos.arboles.rbTree import *

def code_binary_tree():
    st.subheader("Estructura de un árbol")
    st.code(
        '''class Node:
        def __init__(self, value=None, parent = None, is_root = False, is_left = False, is_right = False):
            self.value = value
            self.left = None
            self.right = None
            self.parent = parent
            self.is_root = is_root
            self.is_left = is_left
            self.is_right = is_right

    class BinaryTree:
        def __init__(self):
            self.root = None''', language='python'
    )

    st.subheader("Eventos")
    opcion = st.selectbox(
        "",
        (
            "Vacío(empty)",
            "Agregar(add)",
            "Eliminar(delete)",
            "Buscar(search)",
            "Tamaño(size)", "Recorrer",)
    )

    if opcion == "Vacío(empty)":
        code = '''
        def empty(self):
            if self.root == None:
                return True
            else:
                return False'''
    elif opcion == "Agregar(add)":
        code = '''
        def add(self, value):
            if self.empty():
                self.root = Node(value=value, is_root=True)
            else:
                node = self.__get_place(value)
                if value <= node.value:
                    node.left = Node(value=value, parent=node, is_left=True)
                else:
                    node.right = Node(value=value, parent=node, is_right=True)'''
    elif opcion == "Eliminar(delete)":
        code = '''
        def deleteDeepest(self, d_node):
            q = []
            q.append(self.root)
            while(len(q)):
                temp = q.pop(0)
                if temp is d_node:
                    temp = None
                    return
                if temp.right:
                    if temp.right is d_node:
                        temp.right = None
                        return
                    else:
                        q.append(temp.right)
                if temp.left:
                    if temp.left is d_node:
                        temp.left = None
                        return
                    else:
                        q.append(temp.left)

        def delete(self, key):
            root = self.root
            if root == None:
                return None
            if root.left == None and root.right == None:
                if root.key == key:
                    return None
                else:
                    return root
            key_node = None
            q = []
            q.append(root)
            temp = None
            while(len(q)):
                temp = q.pop(0)
                if temp.value == key:
                    key_node = temp
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            if key_node:
                x = temp.value
                self.deleteDeepest(temp)
                key_node.value = x
            return root'''
    elif opcion == "Buscar(search)":
        code = """
        def search(self, node, value):
            if node == None:
                return None
            else:
                if node.value == value:
                    return node
                elif value <= node.value:
                    return self.seach(node.left, value)
                else:
                    return self.search(node.right, value)"""
    elif opcion == "Tamaño(size)":
        code = '''
        def __count_nodes(self, node):
            if node is None:
                return 0
            return 1 + self.__count_nodes(node.left) + self.__count_nodes(node.right)
        
        def size(self):
            return self.__count_nodes(self.root)'''
    elif opcion == "Recorrer":
        code = '''
        def show_in_order(self, node):
            # izquierda - raiz - derecha
            if node:
                self.show_in_order(node.left)
                print(node.value)
                self.show_in_order(node.right)

        def show_pre_order(self, node):
            #  raiz - izquierda - derecha
            if node:
                print(node.value)
                self.show_pre_order(node.left)
                self.show_pre_order(node.right)

        def show_pos_order(self, node):
            #Izquierda - derecha - raiz
            if node:
                self.show_pos_order(node.left)
                self.show_pos_order(node.right)
                print(node.value)'''
    st.code(code, language='python')

def ejercicio1():
    opcion = st.selectbox(
        "1.Escribe una función (o dos) que realice la reflexión de un árbol binario",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        code = '''
            def reflect_tree(tree):
                reflect_tree_recursive(tree.root)
                
            def reflect_tree_recursive(node):
                if node is None:
                    return
                # Intercambiar los nodos izquierdo y derecho
                node.left, node.right = node.right, node.left
                # Reflexionar los subárboles izquierdo y derecho
                reflect_tree_recursive(node.left)
                reflect_tree_recursive(node.right)

            print("Árbol antes de la reflexión:")
            tree.show_in_order(tree.root)

            reflect_tree(tree)

            print("Árbol después de la reflexión:")
            tree.show_in_order(tree.root)'''
        st.code(code, language='python')
    
def ejercicio2():
    opcion = st.selectbox(
        "2.Con la lista de números enteros [5, 8, 3, 2, 9, 1, 7], encuentra el número máximo en esa lista",
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        code = '''
        def max_value(tree):
            if tree.root is None:
                return None

            node = tree.root
            while node.right is not None:
                node = node.right

            return node.value
        numbers = [5, 8, 3, 2, 9, 1, 7]

        tree = BinaryTree()
        for number in numbers:
            tree.add(number)

        max_number = tree.max_value()
        print("El número máximo es:", max_number)'''
        st.code(code, language='python')

def ejercicio3():
    opcion = st.selectbox(
        '3.Encuentra la palabra más larga que se encuentre en una lista determinada',
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        code = '''
            def max_length_word(tree):
                if tree.root is None:
                    return None

                node = tree.root
                while node.right is not None:
                    node = node.right

                return node.value
            words = ["apple", "banana", "cherry", "grapefruit", "kiwi", "orange"]

            tree = BinaryTree()
            for word in words:
                tree.add(word)

            longest_word = tree.max_length_word()
            print("La palabra más larga es:", longest_word)'''
        st.code(code, language='python')

def insertar_nodos_rbTree():
    tree = RedBlackTree()
    # Verifica si la lista ya existe en el estado de la sesión
    if 'lista_numeros' not in st.session_state:
        st.session_state.lista_numeros = []  # Crea una lista vacía en el estado de la sesión

    # Crea un campo de entrada numérica
    numero = st.number_input("Ingresa un número")

    # Agrega el número ingresado a la lista cuando se hace clic en el botón
    if st.button("Agregar"):
        st.session_state.lista_numeros.append(numero)
    
    for numero in st.session_state.lista_numeros:
        tree.insert(numero)
    tree.plot_tree()

def codigo_huffman():
    code = '''
        from heapq import heappush, heappop, heapify
        from collections import defaultdict

        # Función auxiliar para crear un árbol de Huffman
        def construir_arbol_huffman(freq):
            heap = [[peso, [símbolo, ""]] for símbolo, peso in freq.items()]
            heapify(heap)
            while len(heap) > 1:
                lo = heappop(heap)
                hi = heappop(heap)
                for par in lo[1:]:
                    par[1] = '0' + par[1]
                for par in hi[1:]:
                    par[1] = '1' + par[1]
                heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
            return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

        # Función para codificar el mensaje
        def codificar_huffman(datos):
            freq = defaultdict(int)
            for char in datos:
                freq[char] += 1
            if not freq:
                return "", None
            arbol_huff = construir_arbol_huffman(freq)
            huff_dict = {char: code for char, code in arbol_huff}
            encoded = "".join(huff_dict[char] for char in datos)
            return encoded, arbol_huff

        # Función para decodificar el mensaje
        def decodificar_huffman(datos_codificados, arbol_huff):
            if not arbol_huff:
                return ""
            dec_dict = {code: char for char, code in arbol_huff}
            codigo_actual = ""
            decoded = ""
            for bit in datos_codificados:
                codigo_actual += bit
                if codigo_actual in dec_dict:
                    decoded += dec_dict[codigo_actual]
                    codigo_actual = ""
            return decoded'''
    st.code(code, language='python')


    
