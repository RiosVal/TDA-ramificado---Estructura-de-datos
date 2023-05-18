from codigos.arboles.AVLTree import *


def impAVL():
    """Crea un árbol AVL (Árbol de Búsqueda y Equilibrio Automático) y luego lo muestra gráficamente utilizando Streamlit
    """
    avl_tree = AVLTree()
    root = None

    # Insertar nodos en el árbol
    root = avl_tree.insert(root, 10)
    root = avl_tree.insert(root, 20)
    root = avl_tree.insert(root, 30)
    root = avl_tree.insert(root, 40)
    root = avl_tree.insert(root, 50)

    # Graficar el árbol AVL en Streamlit
    avl_tree.plot_tree(root)
