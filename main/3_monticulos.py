import streamlit as st
from codigos.monticulos.monticulos import *
from codigos.monticulos.ejercicios import *
from codigos.monticulos.rbHeaps import *


def intro():
    """
    Esta funcion muestra en pantalla la informacion basica de los monticulos
    """

    st.header('⛰️')
    st.write("<h1>Monticulos</h1>", unsafe_allow_html=True) # Título principal usando etiquetas HTML
    st.write( # Descripción de los montículos utilizando etiquetas HTML
        """
            <div style="text-align: justify;"><p> 
            Los montículos (Heaps) son estructuras de datos que permite la extracción de los
            mismos de forma ordenada. Existen dos tipos: los montículos máximos, que
            permite ex  traer los elementos en orden decreciente y los montículos mínimos, en
            que la extracción se inicia por el más pequeño y termina con el valor máximo.
            </p></div>
        """,
        unsafe_allow_html=True
    )


    botonCodeHeap = st.empty()  
    mostrar = botonCodeHeap.button("Mostrar codigo")

    if mostrar: #Verifica si el boton se ha activado
        botonCodeHeap.empty()
        st.button("Ocultar código")
        codeMonticulos()


def monticulosMaxMin():
    """
    Esta funcion muestra en pantalla toda la informacion de monticulos maximos y minimos.
    """

    st.write('<h2>Monticulos maximos y minimos</h2>', unsafe_allow_html=True)

    st.image("images/monticulos/max-min-heap.png")

    heapMin, heapMax = st.tabs(["Monticulos Minimos", "Monticulos Maximos"]) 
    #Se crea una tabla para mostrar la informacion de los dos monticulos

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
        
        #Se hace llamado a la siguiente funcion, la cual muestra en pantalla el codigo de monticulos minimos en python
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

        #Se hace llamado a la siguiente funcion, la cual muestra en pantalla el codigo de monticulos maximos en python
        codeMonticuloMax()


def importante_saber():
    """
    Esta funcion muestra en pantalla informacion importante sobre el tema principal "Monticulos"
    """

    st.markdown("<h2>Importante entender</h2>", unsafe_allow_html=True)
    st.markdown("Los monticulos se componen de los mismos elementos que componen a un arbol binario, estos tienen los mismos componentes que hacen un arbol binario'Revisar arboles- Definiciones importantes '", unsafe_allow_html=True)

    #Se definen 3 columnas para organizar la informacion
    

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
        Cuando se trata de arbol binario se debe cumplir dos propiedades esenciales para que sea considerado un monticulo, estas son: 
        - EL arbol binario debe estar completo, que quiere decir esto que todos los niveles del arbol 
        deben estar completos, a exepcion del ultimo que su funcion es completar desde la izquierda.
        - El arbol debe estar ordenado de manera por niveles ya sea de manera acedente o descendente.
        '''
        '''
        A partir de esto se pueden clasificar en 
        montículos de orden máximo o de orden mínimo, en donde cada padre de los primeros es mayor 
        que sus hijos y en los segundos los padres son menores que sus hijos.
        '''
    )

#Diferencias entre monticulos y arboles 
def diferencia():
    st.subheader('Como podemos diferenciar un arbol y un monticulo?')
    st.markdown('''
                Un árbol binario es una estructura de datos compuesta por nodos que están organizados de manera jerárquica. Cada nodo puede tener hasta dos nodos hijos: un hijo izquierdo y un hijo derecho. 
                Algunas características distintivas de un árbol binario son:
                - Estructura jerárquica: Los nodos en un árbol binario están organizados en niveles jerárquicos, donde cada nodo puede tener hasta dos nodos hijos. Existe un nodo raíz que es el nodo superior y a partir de él se ramifican los nodos hijos.
                - Nodos hijos: Cada nodo en un árbol binario puede tener como máximo dos nodos hijos. El hijo izquierdo se encuentra a la izquierda del nodo y el hijo derecho se encuentra a la derecha. Estos nodos hijos pueden, a su vez, tener sus propios hijos, formando así una estructura recursiva.
                - Ordenamiento: Dependiendo de la implementación del árbol binario, puede haber una relación de orden entre los valores almacenados en los nodos. Por ejemplo, en un árbol binario de búsqueda, el valor almacenado en el nodo izquierdo es menor que el valor almacenado en el nodo padre, y el valor almacenado en el nodo derecho es mayor.
                '''
                '''
                Por otro lado, en informática, un montículo (también conocido como heap) es una estructura de datos que satisface una propiedad especial llamada "propiedad del montículo". Algunas características distintivas de un montículo son:
                - Propiedad del montículo: Un montículo cumple con la propiedad del montículo, que puede ser de dos tipos: montículo máximo o montículo mínimo. En un montículo máximo, el valor almacenado en cada nodo es mayor o igual que los valores almacenados en sus nodos hijos. En un montículo mínimo, el valor almacenado en cada nodo es menor o igual que los valores almacenados en sus nodos hijos.
                - Estructura completa: Un montículo se puede representar mediante un árbol binario completo, lo que significa que todos los niveles del árbol están completamente llenos, excepto posiblemente el último nivel, que se llena de izquierda a derecha. Esta estructura completa permite una representación eficiente del montículo utilizando un arreglo.
                - Operaciones de inserción y extracción: Los montículos suelen utilizarse para implementar colas de prioridad, ya que permiten la inserción eficiente de elementos y la extracción del elemento de mayor o menor prioridad según el tipo de montículo. Las operaciones de inserción y extracción mantienen la propiedad del montículo.
                ''')




def tabsArbol():
    """
        Esta funcion contiene informacion sobre lo que contiene un monticulo, la informacion se muestra
        haciendo uso de las tablas "st.tabs" para un mejor orden
    """
    
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
    """
        Esta funcion muestra en pantalla ejercicios practicos para entender mejor el tema, haciendo
    """
    st.write('<div style="text=align: center;"><h2>Ejercicios</h2></div>', unsafe_allow_html=True)
    st.write("""A continuación te mostraremos ejercicios para que apliques lo aprendido, la solución se muestra una vez indiques en el botón
            que quieres verla, sin embargo te recomendamos que intentes resolverlo tu solo para tu mejor comprensión. Recuerda que la mejor manera de 
            aprender es haciéndolo tu mismo.""")
    
    #Se hace el llamado de los ejercicios ubicados en ./codigos/monticulos/ejercicios.py para mostrarlos en pantalla
    ejercicio1()
    ejercicio2()
    ejercicio3()




def tipos():
    """
        Mediante el uso de "St.tabs" se muestra la informacion de otros tipos de monticulos y sus caracteristicas
    """
    
    st.write("<h2>Otros tipos de monticulos</h2>", unsafe_allow_html=True)
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

def page():
    """
        Esta funcion muestra la introduccion y el menu para desplegar cada parte del tema individual, para un mejor orden
    """
    intro()
    opcion = st.selectbox(
        'Escoge el tema a desplegar',
        (
            '',
            'Definiciones importantes',
            'Monticulos MaxMin',
            'Tipos de monticulos',
            'Aplicacion TDA',
            'Ejercicios básicos de comprensión',
            'Ejercicio de aplicación'
        )
    )
    if opcion == 'Definiciones importantes':
        importante_saber()
        tabsArbol()
        diferencia()    
    elif opcion =='Monticulos MaxMin':
        monticulosMaxMin()
    elif opcion == 'Tipos de monticulos':
        tipos()
    elif opcion == 'Aplicacion TDA':
        tda_monticulos()
    elif opcion == 'Ejercicios básicos de comprensión':
        ejercicios()
    elif opcion == 'Ejercicio de aplicación':
        st.write('EJERCICIO AQUÍ...')

#Se llama a la funcion de pagina principal de los monticulos
page()