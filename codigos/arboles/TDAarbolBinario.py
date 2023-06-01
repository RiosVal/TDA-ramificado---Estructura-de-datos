import matplotlib.pyplot as plt
import streamlit as st

class Node:
    def __init__(self, value=None, parent=None, is_root=False, is_left=False, is_right=False):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.is_root = is_root
        self.is_left = is_left
        self.is_right = is_right

class BinaryTree:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root is None

    def add(self, value):
        if self.empty():
            self.root = Node(value=value, is_root=True)
        else:
            node = self.__get_place(value)
            if value <= node.value:
                node.left = Node(value=value, parent=node, is_left=True)
            else:
                node.right = Node(value=value, parent=node, is_right=True)

    def __get_place(self, value):
        current = self.root
        parent = None

        while current:
            parent = current
            if value <= current.value:
                current = current.left
            else:
                current = current.right

        return parent

    def search(self, value):
        return self.__search_recursive(self.root, value)

    def __search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self.__search_recursive(node.left, value)
        else:
            return self.__search_recursive(node.right, value)

    def delete(self, value):
        self.root = self.__delete_recursive(self.root, value)

    def __delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self.__delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self.__delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Encontrar el sucesor en orden para mantener las propiedades del árbol binario de búsqueda
            successor = self.__find_min(node.right)
            node.value = successor.value
            node.right = self.__delete_recursive(node.right, successor.value)

        return node

    def __find_min(self, node):
        while node.left:
            node = node.left
        return node

    def size(self):
        return self.__count_nodes(self.root)

    def __count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.__count_nodes(node.left) + self.__count_nodes(node.right)

    def show_in_order(self):
        self.__show_in_order_recursive(self.root)

    def __show_in_order_recursive(self, node):
        if node:
            self.__show_in_order_recursive(node.left)
            print(node.value)
            self.__show_in_order_recursive(node.right)

    def plot(self):
        if self.empty():
            st.write("El árbol está vacío.")
            return
        
        fig, ax = plt.subplots()
        self.plot_node(ax, self.root)
        ax.axis("off")
        
        # Mostrar la figura en Streamlit
        st.pyplot(fig)

    def plot_node(self, ax, node, x=0, y=0, level=1, dx=100, dy=50):
        if node is None:
            return
        
        ax.text(x, y, str(node.value), color="black", weight="bold", ha="center", va="center",
                bbox=dict(facecolor="white", edgecolor="black"))

        if node.left:
            x_left = x - dx * (1 / 2) ** level
            y_left = y - dy
            ax.plot([x, x_left], [y, y_left], color="black", linestyle="-")
            self.plot_node(ax, node.left, x_left, y_left, level + 1, dx, dy)

        if node.right:
            x_right = x + dx * (1 / 2) ** level
            y_right = y - dy
            ax.plot([x, x_right], [y, y_right], color="black", linestyle="-")
            self.plot_node(ax, node.right, x_right, y_right, level + 1, dx, dy)
