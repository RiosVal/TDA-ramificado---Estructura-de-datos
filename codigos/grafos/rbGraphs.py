

import matplotlib.pyplot as plt
import streamlit as st

class RBNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = "red"


class RedBlackTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.root = self.nil

    def insert(self, key):
        node = RBNode(key)
        node.left = self.nil
        node.right = self.nil
        node.color = "red"

        y = None
        x = self.root

        while x != self.nil:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y

        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "black"
            #self.plot_tree()  # Graficar árbol después de la inserción
            return

        self.fix_insert(node)
        #self.plot_tree()  # Graficar árbol después de la inserción

    def fix_insert(self, node):
        while node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)

            if node == self.root:
                break

        self.root.color = "black"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y


    def plot_node(self, ax, node, x=0, y=0, level=1, dx=100, dy=50):
        if node == self.nil:
            return

        # Plot current node
        color = "red" if node.color == "red" else "black"
        ax.text(x, y, str(node.key), color=color, weight="bold", ha="center", va="center",
                bbox=dict(facecolor="white", edgecolor=color))

        # Plot left subtree
        if node.left != self.nil:
            x_left = x - dx * (1 / 2) ** level
            y_left = y - dy
            ax.plot([x, x_left], [y, y_left], color=color, linestyle="-")
            self.plot_node(ax, node.left, x_left, y_left, level + 1, dx, dy)

        # Plot right subtree
        if node.right != self.nil:
            x_right = x + dx * (1 / 2) ** level
            y_right = y - dy
            ax.plot([x, x_right], [y, y_right], color=color, linestyle="-")
            self.plot_node(ax, node.right, x_right, y_right, level + 1, dx, dy)

    def plot_tree(self):
        fig, ax = plt.subplots()
        self.plot_node(ax, self.root)
        ax.axis("off")
        st.pyplot(fig)