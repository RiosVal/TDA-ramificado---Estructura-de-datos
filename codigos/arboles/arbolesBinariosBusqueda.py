import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

# Definición de la clase Nodo para el árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Definición de la clase ÁrbolBinario
class ÁrbolBinario:
    def __init__(self):
        self.raíz = None

    # Función para insertar un nuevo nodo en el árbol
    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.raíz is None:
            self.raíz = nuevo_nodo
        else:
            actual = self.raíz
            while True:
                if valor < actual.valor:
                    if actual.izquierda is None:
                        actual.izquierda = nuevo_nodo
                        break
                    else:
                        actual = actual.izquierda
                elif valor > actual.valor:
                    if actual.derecha is None:
                        actual.derecha = nuevo_nodo
                        break
                    else:
                        actual = actual.derecha

    # Función para buscar un valor en el árbol
    def buscar(self, valor):
        if self.raíz is None:
            return False
        else:
            actual = self.raíz
            while actual is not None:
                if valor == actual.valor:
                    return True
                elif valor < actual.valor:
                    actual = actual.izquierda
                else:
                    actual = actual.derecha
            return False


    def eliminar(self, valor):
        if self.raíz is None:
            return False
        else:
            # Buscar el nodo a eliminar
            encontrado = False
            actual = self.raíz
            padre = None
            while actual and not encontrado:
                if valor == actual.valor:
                    encontrado = True
                elif valor < actual.valor:
                    padre = actual
                    actual = actual.izquierda
                else:
                    padre = actual
                    actual = actual.derecha
            
            if actual is None:
                return False
            
            # Caso 1: el nodo a eliminar es una hoja
            if actual.izquierda is None and actual.derecha is None:
                if padre is not None:
                    if padre.izquierda == actual:
                        padre.izquierda = None
                    else:
                        padre.derecha = None
                else:
                    self.raíz = None
            
            # Caso 2: el nodo a eliminar tiene un solo hijo
            elif actual.izquierda is None:
                if padre is not None:
                    if padre.izquierda == actual:
                        padre.izquierda = actual.derecha
                    else:
                        padre.derecha = actual.derecha
                else:
                    self.raíz = actual.derecha
            
            elif actual.derecha is None:
                if padre is not None:
                    if padre.izquierda == actual:
                        padre.izquierda = actual.izquierda
                    else:
                        padre.derecha = actual.izquierda
                else:
                    self.raíz = actual.izquierda
            
            # Caso 3: el nodo a eliminar tiene dos hijos
            else:
                padre = actual
                sucesor = actual.derecha
                while sucesor.izquierda:
                    padre = sucesor
                    sucesor = sucesor.izquierda
                actual.valor = sucesor.valor
                if padre.derecha == sucesor:
                    padre.derecha = sucesor.derecha
                else:
                    padre.izquierda = sucesor.derecha
            
            return True

    def graficar(self):
        def graficar_arbol(nodo, nivel=0, posx=0, posy=0):
            if nodo is None:
                return

            radio = 500
            desplazamiento_vertical = 1000

            if nodo.izquierda:
                nueva_posx = posx - radio / (2 ** (nivel + 1))
                nueva_posy = posy - desplazamiento_vertical
                plt.plot([posx, nueva_posx], [posy, nueva_posy], 'k-')
                graficar_arbol(nodo.izquierda, nivel + 1, nueva_posx, nueva_posy)

            if nodo.derecha:
                nueva_posx = posx + radio / (2 ** (nivel + 1))
                nueva_posy = posy - desplazamiento_vertical
                plt.plot([posx, nueva_posx], [posy, nueva_posy], 'k-')
                graficar_arbol(nodo.derecha, nivel + 1, nueva_posx, nueva_posy)

            plt.text(posx, posy, str(nodo.valor), fontsize=12, ha='center', va='center',
                     bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

            if nivel == 0:
                plt.axis('off')
                st.pyplot(plt.gcf())

        graficar_arbol(self.raíz)
