import streamlit as st
from codigos.monticulos.monticulos import *
from codigos.monticulos.ejercicios import *
from codigos.monticulos.rbHeaps import *


def intro():
    st.header('⛰️')
    st.write("<h1>Monticulos</h1>", unsafe_allow_html=True)
    st.write(
        """
            <div style="text-align: justify;"><p> 
            Los montículos (Heaps) son estructuras de datos que permite la extracción de los
            mismos de forma ordenada. Existen dos tipos: los montículos máximos, que
            permite extraer los elementos en orden decreciente y los montículos mínimos, en
            que la extracción se inicia por el más pequeño y termina con el valor máximo.
            </p></div>
        """,
        unsafe_allow_html=True
    )
    botonCodeHeap = st.empty()
    mostrar = botonCodeHeap.button("Mostrar codigo")

    if mostrar:
        botonCodeHeap.empty()
        st.button("Ocultar código")
        codeMonticulos()


def monticulosMaxMin():

    st.write('<h2>Monticulos maximos y minimos</h2>', unsafe_allow_html=True)

    st.image("images/monticulos/max-min-heap.png")

    heapMin, heapMax = st.tabs(["Monticulos Minimos", "Monticulos Maximos"])

    with heapMin:
        st.write("""<div style="text-align: center;"><h2>Monticulos Minimos</h2></div>""", unsafe_allow_html=True)
        st.write("""<div style="text-align: justify;">Un montículo mínimo es similar a un montículo máximo, pero en este caso, el valor de cada nodo es 
                    menor o igual que el valor de sus nodos hijos. El nodo raíz tiene el valor mínimo en todo el montículo y, para 
                    cualquier nodo en el montículo, el valor de sus hijos es mayor o igual al suyo.""", unsafe_allow_html=True)
        st.write("<br><h5>Caracteristicas:</h5>", unsafe_allow_html=True)     
        st.write("""
                    - El elemento de menor valor se encuentra en la raíz del montículo.
                    - Permite acceder rápidamente al mínimo elemento del montículo.
                    - Para cualquier nodo del montículo, el valor de ese nodo es mayor o igual que el valor de sus nodos descendientes (propiedad del montículo mínimo).
                    """, unsafe_allow_html=True)

        st.write("<h5>Codigo en python:</h5>", unsafe_allow_html=True)
        codeMonticuloMin()

    with heapMax:
        st.write("""<div style="text-align: center;"><h2>Monticulos Maximos</h2></div>""", unsafe_allow_html=True)
        st.write("""<div style="text-align: justify;">Un montículo máximo es una estructura de datos en 
                    la que el valor de cada nodo es mayor o igual que el valor de sus nodos hijos. Es decir, el nodo raíz 
                    tiene el valor máximo en todo el montículo y para cualquier nodo en el montículo, el valor de sus hijos 
                    es menor o igual al suyo.</div>""", unsafe_allow_html=True)     
        st.write("<br><h5>Caracteristicas:</h5>", unsafe_allow_html=True)
        st.write("""
                    - El elemento de mayor valor se encuentra en la raíz del montículo.
                    - Permite acceder rápidamente al máximo elemento del montículo.
                    - Para cualquier nodo del montículo, el valor de ese nodo es menor o igual que el valor de sus nodos descendientes (propiedad del montículo máximo).
                    """, unsafe_allow_html=True)

        st.write("<h5>Codigo en python:</h5>", unsafe_allow_html=True)
        codeMonticuloMax()


def importante_saber():
    
    st.markdown("<h2>Importante entender</h2>", unsafe_allow_html=True)
    st.markdown("Los monticulos se componen de los siguientes elementos:", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<b>Nodo</b>: cada elemento que contiene un árbol", unsafe_allow_html=True)
        st.markdown("<b>Nodo raíz</b>: primer nodo de un árbol", unsafe_allow_html=True)
        st.markdown("<b>Nodo padre</b>: aquellos nodos que tienen al menos un hijo y está directamente superior a el", unsafe_allow_html=True)
        st.markdown("<b>Nodo hijo</b>: todos quellos que tienen un padre", unsafe_allow_html=True)    
        st.markdown("<b>Nodo hermano</b>: los nodos que comparten a un mismo padre", unsafe_allow_html=True)
        st.markdown("<b>Nodo hoja</b>: nodos que no tienen hijos", unsafe_allow_html=True)
        st.markdown("<b>Nodo rama</b>: aquellos nodos que no son raíz y tienen al menos un hijo", unsafe_allow_html=True)
        st.markdown("<b>Decendiente</b>: nodo que está en un nivel inferior en relación con otro nodo específico", unsafe_allow_html=True)
    with col2:
        st.markdown("<b>Ancestro</b>: nodo que está en un nivel superior en relación con otro nodo específico", unsafe_allow_html=True)
        st.markdown("<b>Nodo interno</b>: nodo que tiene al menos un hijo", unsafe_allow_html=True)
        st.markdown("<b>Camino</b>: secuencia de nodos conectados entre sí en el árbol", unsafe_allow_html=True)
        st.markdown("<b>Nivel de un nodo</b>: posición relativa de un nodo en el árbol", unsafe_allow_html=True)
        st.markdown("<b>Nivel de un árbol</b>: es el nivel más alto entre todos los nodos del árbol", unsafe_allow_html=True)
        st.markdown("<b>Altura de un nodo</b>: es la longitud del camino más largo desde ese nodo hasta un nodo terminal", unsafe_allow_html=True)
        st.markdown("<b>Altura de un árbol</b>: es la longitud máxima del camino desde la raíz hasta el nodo más alejado", unsafe_allow_html=True)
    with col3:
        st.markdown("<b>Peso de un árbol</b>: suma de los persos de todos los nodos de ese árbol", unsafe_allow_html=True)
        st.markdown("<b>Orden</b>: número máximo de hijos que puede tener un nodo", unsafe_allow_html=True)
        st.markdown("<b>Grado</b>: numero mayor d ehijos que tiene alguno de los nodos del árbol", unsafe_allow_html=True)
        st.markdown("<b>Profundidad</b>: distancia entre un nodo dado y la raíz del árbol", unsafe_allow_html=True)
        st.markdown("<b>Bosque</b>: coleccion de árboles disjuntos, donde cada átbol puede tener su propia raíz y nodos", unsafe_allow_html=True)
        st.markdown("<b>Sub-árbol</b>: es todo árbol generado a partir de una sección determinada del árbol", unsafe_allow_html=True)
        st.markdown("<b>Peso de un nodo</b>: valor asociado o atributo numérico asociado al nodo", unsafe_allow_html=True)
#Caracteristicas de los monticulos 
    st.subheader('Caracteristicas:')
    st.markdown(
        '''
        - Todos los monticulos son arboles binarios.
        - El árbol está completamente balanceado excepto el último nivel, que debe
            estar lleno de izquierda a derecha.
        - Para un elemento del heap en la posición k, sus hijos deberán estar en las
            posiciones 2k y 2k+1 del heap.
        - Un heap puede representarse en un arreglo.
        - Toda lista ordenada es un monticulo.
        '''
    )
# Carateristicas de los monticulos 
    st.subheader('Propiedades:')
    st.markdown(
        '''
        - Un árbol binario completamente lleno, con la posible excepción del nivel
            más bajo, el cual se rellena de izquierda a derecha. Estos árboles se
            denominan árboles binarios completos.
        - Todo nodo debe ser mayor que todos sus descendientes. Por lo tanto, el
            máximo estará en la raíz y su búsqueda y eliminación se podrá realizar
            rápidamente.
        '''
    )

def tabsArbol():
    
    tab1, tab2, tab3, tab4 = st.tabs(["Árbol", "Raíz, rama, hoja", "Nodos padre e hijos", "Hermanos"])

    with tab1:
        st.image("images/arboles/arbol.png")
    with tab2:
        st.image("images/arboles/padreHermanos.png")
    with tab3:
        st.image("images/arboles/padreHijo.png")
    with tab4:
        st.image("images/arboles/RaizRamaHoja.png")


def ejercicios():
    st.write('<div style="text=align: center;"><h2>Ejercicios</h2></div>', unsafe_allow_html=True)
    st.write("""A continuación te mostraremos ejercicios para que apliques lo aprendido, la solución se muestra una vez indiques en el botón
            que quieres verla, sin embargo te recomendamos que intentes resolverlo tu solo para tu mejor comprensión. Recuerda que la mejor manera de 
            aprender es haciéndolo tu mismo.""")
    ejercicio1()
    ejercicio2()
    ejercicio3()




def tipos():
    st.write("<br><h2>Otros tipos de monticulos</h2>", unsafe_allow_html=True)
    tipo1, tipo2, tipo3, tipo4, tipo5 = st.tabs(["Binomial", "Fibonacci", "Paridad", "Leftist", "Par Binario"])

    with tipo1: #Info Monticulo Binomial
        st.write("<h3>Montículo binomial:</h3>", unsafe_allow_html=True)
        st.write("""<div style="text-align: justify;">Un montículo binomial es una colección de árboles binomiales, 
                    donde cada árbol binomial cumple con las propiedades de un montículo mínimo. Los montículos binomiales 
                    son útiles en algoritmos de mezcla y en la implementación eficiente de colas de prioridad.</div>""", unsafe_allow_html=True)
        st.write("<br><h5>Caracteristicas:</h5>", unsafe_allow_html=True)
        st.write("""
                    - Utiliza árboles binomiales para representar la estructura de datos.
                    - Cada árbol binomial cumple con la propiedad del montículo binomial, donde el valor de cada nodo es mayor o igual que el valor de su padre.
                    - Permite las operaciones de inserción, unión y extracción del mínimo en tiempo logarítmico.
                    - La unión de dos montículos binomiales se realiza combinando los árboles binomiales del mismo grado en una estructura jerárquica.
                    """, unsafe_allow_html=True)
    
    with tipo2:
        st.write("<h3>Montículo fibonacci:</h3>", unsafe_allow_html=True)
        st.write("""<div style="text-align: justify;">Un montículo de Fibonacci es similar a un montículo 
                    binomial, pero permite operaciones más eficientes de unión y disminución de clave. Además, 
                    se caracteriza por mantener un conjunto de árboles binomiales de grado limitado, lo que resulta 
                    en una mejor eficiencia en el tiempo de ejecución</div>""", unsafe_allow_html=True)
        st.write("<br><h5>Caracteristicas:</h5>", unsafe_allow_html=True)
        st.write("""
                    - Utiliza árboles de Fibonacci para representar la estructura de datos.
                    - Cada árbol de Fibonacci cumple con la propiedad del montículo de Fibonacci, donde el valor de cada nodo es mayor o igual que el valor de su padre.
                    - Permite las operaciones de inserción, unión y extracción del mínimo en tiempo amortizado constante.
                    - Los árboles de Fibonacci se combinan durante las operaciones de unión para mantener una estructura equilibrada.
                    """, unsafe_allow_html=True)
    
    with tipo3:
        st.write("<h3>Montículo paridad:</h3>", unsafe_allow_html=True)
        st.write("""<div style="text-align: justify;">Un montículo de paridad es una variante de los montículos 
                    binarios, donde los nodos se organizan de acuerdo con su valor y su paridad. Los nodos de paridad 
                    par tienen prioridad sobre los nodos de paridad impar.</div>""", unsafe_allow_html=True)
        st.write("<br><h5>Caracteristicas:</h5>", unsafe_allow_html=True)
        st.write("""
                    - Utiliza un esquema de paridad para representar la estructura de datos.
                    - Cada nodo en el montículo de paridad tiene un bit de paridad asociado, que indica si el número de descendientes es par o impar.
                    - Permite las operaciones de inserción, unión y extracción del mínimo en tiempo logarítmico.
                    - La unión de dos montículos de paridad se realiza combinando los árboles en función de la paridad de sus raíces.
                    """, unsafe_allow_html=True)
    
    with tipo4:
        st.write("<h3>Montículo leftist:</h3>", unsafe_allow_html=True)
        st.write("""<div style="text-align: justify;">Un montículo de leftist es un tipo de montículo binario que 
                    se basa en la propiedad de "peso izquierdo". Cada nodo almacena la distancia más corta al nodo más 
                    lejano en su subárbol derecho. Esto permite operaciones eficientes de unión y se utiliza en algoritmos 
                    como el algoritmo de unión ponderada.</div>""", unsafe_allow_html=True)
        st.write("<br><h5>Caracteristicas:</h5>", unsafe_allow_html=True)
        st.write("""
                    - Utiliza árboles leftist para representar la estructura de datos.
                    - Cada árbol leftist cumple con la propiedad del montículo leftist, donde el valor de cada nodo es mayor o igual que el valor de sus hijos.
                    - Permite las operaciones de inserción, unión y extracción del mínimo en tiempo logarítmico.
                    - Los árboles leftist se combinan durante las operaciones de unión para mantener la propiedad de leftist y el orden de los valores.
                    """, unsafe_allow_html=True)
    
    with tipo5:
        st.write("<h3>Montículo par binario:</h3>", unsafe_allow_html=True)
        st.write("""<div style="text-align: justify;">Un montículo de par binario es una variante de los montículos 
                    binarios, donde los nodos se agrupan en pares y el valor de cada nodo del par es menor o igual al 
                    valor del otro nodo. Esto permite la búsqueda y la extracción del mínimo de manera eficiente.</div>""", unsafe_allow_html=True)
        st.write("<br><h5>Caracteristicas:</h5>", unsafe_allow_html=True)
        st.write("""
                    - Utiliza un esquema de par binario para representar la estructura de datos.
                    - Los elementos se almacenan en un arreglo, donde cada índice tiene un bit de paridad asociado.
                    - Permite las operaciones de inserción, unión y extracción del mínimo en tiempo logarítmico.
                    - La unión de dos montículos de par binario se realiza combinando los elementos en función de la paridad de sus índices.
                    """, unsafe_allow_html=True)
def tda_monticulos():
    st.write('''Para la aplicacion de una tda en los monticulos necesitaremos 
    un vector con n elementos que estos seran llamados *heap*este sera util para representar un arbol binario,
    ademas usaremos funciones que definiran cada uno de su funcionamiento''',unsafe_allow_html=True)

    

def page():
    intro()
    opcion = st.selectbox(
        'Escoge el tema a desplegar',
        (
            '',
            'Definiciones importantes',
            'Tipos de monticulos',
            'Monticulos MaxMin',
            'Aplicacion TDA',
            'Ejercicios básicos de comprensión',
            'Ejercicio de aplicación'
        )
    )
    if opcion == 'Definiciones importantes':
        importante_saber()
        tabsArbol()
    elif opcion == 'Tipos de monticulos':
        tipos()
    elif opcion =='Monticulos MaxMin':
        monticulosMaxMin()
    elif opcion == 'Aplicacion TDA':
        tda_monticulos()
    elif opcion == 'Ejercicios básicos de comprensión':
        ejercicios()
    elif opcion == 'Ejercicio de aplicación':
        st.write('EJERCICIO AQUÍ...')

page()
