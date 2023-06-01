import streamlit as st
from codigos.arboles.rbTree import *

def code_binary_tree():
    """Códigos de la estructura y eventos de los árboles binarios y visualización en streamlit
    """
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
    """Ejercicio básico 1
    """
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
    """Ejercicio básico 2
    """
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
    """Ejercicio básico 3
    """
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
    """Árbol interactivo, muestra el árbol en streamlit a medida que el usuario ingresa el valor de los nodos
    """
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
    """Estructura del código de Huffman y visualiación en streamlit
    """
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

def codeAVLtree():
    code_estructura = '''
    class treeNode(object):
    """Definición de la clase treeNode para el árbol AVL 

        Args:
            object (_type_): _description_
        """
        def __init__(self, value):
            self.value = value
            self.l = None
            self.r = None
            self.h = 1
 
 
    class AVLTree(object):'''
    code_insert = '''
    def insert(self, root, key):
        """Implementación de la inserción de un nodo en un árbol AVL

        Args:
            root (treeNode): el nodo raíz del árbol donde se desea insertar el nuevo nodo.
            key (any): el valor del nuevo nodo que se va a insertar.

        Returns:
            treeNode: nodo raíz del árbol actualizado después de la inserción y las rotaciones.
        """
        if not root:
            return treeNode(key)
        elif key < root.value:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)
 
        root.h = 1 + max(self.getHeight(root.l),
                         self.getHeight(root.r))
 
        b = self.getBal(root)
 
        if b > 1 and key < root.l.value:
            return self.rRotate(root)
 
        if b < -1 and key > root.r.value:
            return self.lRotate(root)
 
        if b > 1 and key > root.l.value:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)
 
        if b < -1 and key < root.r.value:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)
 
        return root
    '''
    code_lrotate = '''
    def lRotate(self, z):
        """Rotación hacia la izquierda en un árbol AVL. Se realiza alrededor de un nodo z, que se convierte en el hijo izquierdo del nodo rotado.

        Args:
            z (treeNode):  nodo en torno al cual se realiza la rotación hacia la izquierda.

        Returns:
            treeNode: nuevo nodo raíz después de la rotación hacia la izquierda.
        """
        y = z.r
        T2 = y.l
 
        y.l = z
        z.r = T2
 
        z.h = 1 + max(self.getHeight(z.l),
                      self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                      self.getHeight(y.r))
 
        return y
    '''
    code_rrotate = '''
    def rRotate(self, z):
        """Rotación hacia la derecha en un árbol AVL. Se realiza alrededor de un nodo z, que se convierte en el hijo derecho del nodo rotado.

        Args:
            z (treeNode): nodo en torno al cual se realiza la rotación hacia la derecha.

        Returns:
            treeNode: nuevo nodo raíz después de la rotación hacia la derecha.
        """
        y = z.l
        T3 = y.r
 
        y.r = z
        z.l = T3
 
        z.h = 1 + max(self.getHeight(z.l),
                      self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                      self.getHeight(y.r))
 
        return y
    '''
    code_getHeight = '''
    def getHeight(self, root):
        """Calcula la altura del árbol

        Args:
            root (treeNode): raíz de árbol AVL

        Returns:
            (int): retorna la altura del árbol, 0 si el árbol no tiene raíz.
        """
        if not root:
            return 0
 
        return root.h
    '''
    code_getBal = '''
    def getBal(self, root):
        """Calcula el factor de equilibrio de un nodo en un árbol AVL. El factor de equilibrio se 
        define como la diferencia entre la altura del subárbol izquierdo y la altura del subárbol derecho.

        Args:
            root (treeNode): el nodo para el cual se desea calcular el factor de equilibrio.

        Returns:
            int: Devuelve la diferencia entre estas dos alturas, si el nodo root es None devuelve 0
        """
        if not root:
            return 0
 
        return self.getHeight(root.l) - self.getHeight(root.r)
    '''
    code_preorder = '''
    def preOrder(self, root):
        """Realiza el recorrido en preorden del árbol (nodo raíz, luego el subárbol izquierdo y finalmente el subárbol derecho).

        Args:
            root (treeNode): nodo raíz del árbol
        """
        if not root:
            return
 
        print("{0} ".format(root.value), end="")
        self.preOrder(root.l)
        self.preOrder(root.r)
    '''
    code_search = '''
    def search(self, root, key):
        """Realiza una búsqueda para encontrar si un valor key se encuentra en el árbol.

        Args:
            root (treeNode): nodo raíz del árbol
            key (any):  valor que a buscar

        Returns:
            _type_: _description_
        """
        if not root:
            return False
        elif key == root.value:
            return True
        elif key < root.value:
            return self.search(root.l, key)
        else:
            return self.search(root.r, key)
    '''
    code_delete = '''
    def delete(self, root, key):
        """Elimina un nodo en un árbol AVL

        Args:
            root (treeNode): nodo raíz del árbol en el que se desea eliminar el nodo.
            key (any):  valor del nodo que se desea eliminar.

        Returns:
            treeNode: nodo raíz actualizado después de la eliminación y las rotaciones.
        """
        if not root:
            return root

        elif key < root.value:
            root.left = self.delete(root.left, key)

        elif key > root.value:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right,
                                      temp.value)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    '''
    st.subheader('Estructura de un árbol AVL')
    st.code(code_estructura, language="python")
    st.subheader('Eventos')
    option = st.selectbox(
        "",
        (
            "Insertar (insert)",
            "Rotar a la izquierda (lrotate)",
            "Rotar a la derecha (rRotate)",
            "Altura (get_hight)",
            "Balance (getBal)",
            "Pre orden (preorder)",
            "Buscar (search)",
            "Eliminar (delete)"
        )
    )
    if option == "Insertar (insert)":
        st.code(code_insert, language="python")
    elif option == "Rotar a la izquierda (lrotate)":
        st.code(code_lrotate, language='python')
    elif option == "Rotar a la derecha (rRotate)":
        st.code(code_rrotate, language='python')
    elif option == "Altura (get_hight)":
        st.code(code_getHeight, language='python')
    elif option == "Balance (getBal)":
        st.code(code_getBal, language='python')
    elif option == "Pre orden (preorder)":
        st.code(code_preorder, language='python')
    elif option == "Buscar (search)":
        st.code(code_search, language='python')
    elif option == "Eliminar (delete)":
        st.code(code_delete, language='python')

