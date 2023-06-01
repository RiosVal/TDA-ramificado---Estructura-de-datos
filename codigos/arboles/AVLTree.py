import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

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
 
 
class AVLTree(object):
    """Definición de la clase AVLtree

    Args:
        object (_type_): _description_
    """
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

    def plot_tree(self, root):
        """Crear y muestra la representación gráfica de un árbol AVL en streamlit

        Args:
            root (treeNode): nodo raíz del árbol. 
        """
        G = nx.Graph()
        self._build_graph(G, root, None, None)

        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_size=500, font_size=12, font_weight="bold")

        plt.title("AVL Tree")
        plt.axis("off")

        st.pyplot(plt)

    def _build_graph(self, G, node, parent, direction):
        """Construye el grafo del árbol AVL recursivamente

        Args:
            G (Graph): grafo en construcción
            node (treeNode): nodo actual
            parent (any):  valor del nodo padre
            direction:  indica si el nodo actual es el hijo izquierdo o el hijo derecho del nodo padre
        """
        if node is None:
            return

        G.add_node(node.value)

        if parent is not None:
            G.add_edge(parent, node.value, direction=direction)

        self._build_graph(G, node.l, node.value, "left")
        self._build_graph(G, node.r, node.value, "right")
