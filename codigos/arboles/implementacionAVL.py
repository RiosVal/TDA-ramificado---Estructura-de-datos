from codigos.arboles.AVLTree import *


'''Tree = AVLTree()
root = None
    
root = Tree.insert(root, 10)
root = Tree.insert(root, 20)
root = Tree.insert(root, 30)
root = Tree.insert(root, 40)
root = Tree.insert(root, 50)

print("Arbol en Pre-Order:")
Tree.preOrder(root)

key = 30
if Tree.search(root, key):
    print(f"\n{key} esta en el AVL Tree")
else:
    print(f"\n{key} no esta en el AVL Tree")

key = 32
if Tree.search(root, key):
    print(f"\n{key} esta en el AVL Tree")
else:
    print(f"\n{key} no esta en el AVL Tree")'''

def hola():
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
