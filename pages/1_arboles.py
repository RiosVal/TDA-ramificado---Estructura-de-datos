import streamlit as st
from codigos.arboles.arboles import *
from codigos.arboles.rbTree import *
from codigos.arboles.aplicacionHuffman import uso_huffman
from codigos.arboles.implementacionArbolesBinariosBusqueda import *
from codigos.arboles.implementacionAVL import *
from codigos.arboles.ejercicio_practico import mostrar_prediccion

def intro():
    """Introducción de árboles visualizado en streamlit"""
    st.header("🌳")
    st.title(':green[Árboles]')
    st.write(
        """
        Los árboles son estructuras de datos que se caracterizan por almacenar sus nodos en forma jerárquica, a diferencia de las listas
        que los almacenan en forma lineal.[2]
        """,
    )

def importante_saber():
    """Visualización de definiciones en streamlit"""

    st.header(":green[Importante entender]")
    st.write("""Los árboles se componen de los siguientes elementos:""")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<b>Nodo</b>: cada elemento que contiene un árbol[4]", unsafe_allow_html=True)
        st.markdown("<b>Nodo raíz</b>: primer nodo de un árbol[4]", unsafe_allow_html=True)
        st.markdown("<b>Nodo padre</b>: aquellos nodos que tienen al menos un hijo y está directamente superior a el[2]", unsafe_allow_html=True)
        st.markdown("<b>Nodo hijo</b>: todos quellos que tienen un padre[4]", unsafe_allow_html=True)    
        st.markdown("<b>Nodo hermano</b>: los nodos que comparten a un mismo padre[4]", unsafe_allow_html=True)
        st.markdown("<b>Nodo hoja</b>: nodos que no tienen hijos[4]", unsafe_allow_html=True)
        st.markdown("<b>Nodo rama</b>: aquellos nodos que no son raíz y tienen al menos un hijo[4]", unsafe_allow_html=True)
        st.markdown("<b>Decendiente</b>: nodo que está en un nivel inferior en relación con otro nodo específico[1]", unsafe_allow_html=True)
    with col2:
        st.markdown("<b>Ancestro</b>: nodo que está en un nivel superior en relación con otro nodo específico[4]", unsafe_allow_html=True)
        st.markdown("<b>Nodo interno</b>: nodo que tiene al menos un hijo[1]", unsafe_allow_html=True)
        st.markdown("<b>Camino</b>: secuencia de nodos conectados entre sí en el árbol[4]", unsafe_allow_html=True)
        st.markdown("<b>Nivel de un nodo</b>: posición relativa de un nodo en el árbol[1]", unsafe_allow_html=True)
        st.markdown("<b>Nivel de un árbol</b>: es el nivel más alto entre todos los nodos del árbol[1]", unsafe_allow_html=True)
        st.markdown("<b>Altura de un nodo</b>: es la longitud del camino más largo desde ese nodo hasta un nodo terminal[1]", unsafe_allow_html=True)
        st.markdown("<b>Altura de un árbol</b>: es la longitud máxima del camino desde la raíz hasta el nodo más alejado[1]", unsafe_allow_html=True)
        st.markdown("<b>Peso de un nodo</b>: valor asociado o atributo numérico asociado al nodo[1]", unsafe_allow_html=True)
    with col3:
        st.markdown("<b>Peso de un árbol</b>: suma de los persos de todos los nodos de ese árbol[1]", unsafe_allow_html=True)
        st.markdown("<b>Orden</b>: número máximo de hijos que puede tener un nodo[1]", unsafe_allow_html=True)
        st.markdown("<b>Grado</b>: numero mayor d ehijos que tiene alguno de los nodos del árbol[4]", unsafe_allow_html=True)
        st.markdown("<b>Profundidad</b>: distancia entre un nodo dado y la raíz del árbol[1]", unsafe_allow_html=True)
        st.markdown("<b>Bosque</b>: coleccion de árboles disjuntos, donde cada átbol puede tener su propia raíz y nodos[1]", unsafe_allow_html=True)
        st.markdown("<b>Sub-árbol</b>: es todo árbol generado a partir de una sección determinada del árbol[4]", unsafe_allow_html=True)

def tabs():
    """Visualización de imagenes de árboles en streamlit"""

    tab1, tab2, tab3, tab4 = st.tabs(["Árbol", "Raíz, rama, hoja", "Nodos padre e hijos", "Hermanos"])

    with tab1:
        st.image("images/arboles/arbol.png")
    with tab2:
        st.image("images/arboles/RaizRamaHoja.png")
    with tab3:
        st.image("images/arboles/padreHijo.png")
    with tab4:
        st.image("images/arboles/padreHermanos.png")

def n_arios():
    """Definición de árbol n-ario"""

    st.subheader('Árbol n-ario')
    st.write("Aquellos arboles donde el número máximo de hijos por nodo es de N.[4]")

def reglas_binarios():
    """Visualización de reglas de árboles binarios"""
    st.header("Reglas de los árboles binarios")
    st.markdown(
        """
            - Siempre va a haber un nodo raiz
            - Los datos menores o iguales a la raíz van a la izquierda
            - Los datos mayores van a la derecha de la raíz
        """ 
    )

def binarios():
    """Visualización de la definición de árboles binarios"""
    st.subheader('Árbol binario')
    st.write("Árbol n-ario de Grado 2, cada nodo solo puede tener máximo 2 hijos.[4]")

def codigos_huffman():
    """Visualización de explicación de códigos de Huffman y aplicación interactiva"""
    st.subheader('_Códigos de Huffman_')
    st.write(
        '''El código de Huffman se utiliza para comprimir datos sin pérdida y reducir el tamaño de los datos mediante la eliminación de 
        redundancias en la información. La idea principal detrás del código de Huffman es asignar códigos más cortos a los caracteres 
        que aparecen con más frecuencia en el conjunto de datos, y códigos más largos a los caracteres que aparecen con menos frecuencia. 
        Al hacerlo, se reduce el número total de bits necesarios para representar los datos, lo que reduce el tamaño del archivo.'''
    )
    st.write(
        '''El código de Huffman se utiliza en una amplia variedad de aplicaciones, como la compresión de imágenes, audio y vídeo, y en la 
        transmisión de datos a través de redes de comunicaciones. También se utiliza en la compresión de datos de almacenamiento, 
        como en los archivos ZIP y RAR, que comprimen múltiples archivos en un solo archivo para ahorrar espacio de almacenamiento.'''
    )
    option = st.selectbox(
        "Selecciona la opción 'Huffman' para mostrar el código",
        ('-', 'Huffman')
    )
    if st.button('Mostrar'):
        if option == 'Huffman':
            codigo_huffman()
    st.subheader('_Aplicación del código de Huffman_')    
    uso_huffman()

def usos_binarios():
    """Visualización de los usos de árboles binarios"""
    st.header('Usos')
    st.markdown(
        """
        - Estructuras datos: para almacenar y organizar información de manera eficiente. Los árboles binarios de búsqueda, 
        los árboles AVL y los árboles B son ejemplos de estructuras de datos basadas en árboles que permiten realizar 
        operaciones de búsqueda, inserción y eliminación de manera eficiente.
        - Búsqueda y recuperación de información: Los árboles se utilizan en algoritmos de búsqueda y recuperación de 
        información. Los árboles de búsqueda binarios y los árboles de búsqueda equilibrados como el árbol B son útiles 
        para realizar búsquedas eficientes en grandes conjuntos de datos.
        - Compresión de datos: Los árboles se utilizan en algoritmos de compresión de datos, como el árbol de Huffman, 
        que permite la compresión de datos sin pérdida. Estos árboles asignan códigos de longitud variable a los símbolos 
        de entrada, asignando códigos más cortos a los símbolos más frecuentes y códigos más largos a los menos frecuentes.
        - Análisis y optimización de algoritmos: Los árboles se utilizan para analizar y optimizar el rendimiento de algoritmos. 
        Por ejemplo, el análisis del árbol de recursión se utiliza para determinar la complejidad y eficiencia de algoritmos recursivos.
        - Estructuras de representación y organización: Los árboles se utilizan para representar y organizar estructuras jerárquicas 
        en diversas aplicaciones. Por ejemplo, los árboles se utilizan para representar la estructura de directorios en un sistema de 
        archivos, la estructura de una página web, la jerarquía de categorías en un sistema de gestión de contenidos, entre otros.
        - Inteligencia artificial y aprendizaje automático: Los árboles de decisión y los bosques aleatorios (random forests) 
        se utilizan en aplicaciones de inteligencia artificial y aprendizaje automático para la clasificación y toma de decisiones. 
        Estos árboles se utilizan para construir modelos predictivos basados en reglas de decisión[1].
        """
    )
    codigos_huffman()
    st.subheader('Árboles de búsqueda')
    st.write(
        '''Los árboles de búsqueda binarios son utilizados para buscar y recuperar información de manera 
        eficiente, se utilizan comúnmente en la implementación de bases de datos, la indexación de archivos 
        y la búsqueda de elementos en aplicaciones de búsqueda. También son utilizados en algoritmos de 
        ordenamiento y en la implementación de estructuras de datos como colas de prioridad y conjuntos'''
    )
    arbol_busqueda = insertar_nodos()
    buscar_eliminar_nodo(arbol_busqueda)
    arbol_busqueda.graficar()

def binarios_busqueda():
    """Visualización de información sobre árboles binarios de búsqueda"""
    st.header('Árboles binarios de búsqueda')
    st.write(
        '''
            Los árboles de búsqueda binarios son utilizados para buscar y recuperar información de manera eficiente, se utilizan comúnmente 
            en la implementación de bases de datos, la indexación de archivos y la búsqueda de elementos en aplicaciones de búsqueda. 
            También son utilizados en algoritmos de ordenamiento y en la implementación de estructuras de datos como colas de 
            prioridad y conjuntos[3]
        '''
    )
    usos_binarios()

def arbolesAVL():
    """Visualización de información sobre árboles binarios de búsqueda avanzados junto con su implementación"""
    st.header('Árboles de búsqueda avanzados (AVL)')
    st.write(
        '''AVL es una estructura de datos de árbol binario de búsqueda balanceado. En un árbol AVL, la diferencia de altura entre los 
        subárboles izquierdo y derecho de cada nodo es como máximo uno, lo que garantiza que el árbol esté siempre balanceado, este 
        modelo es útil en situaciones en las que es necesario mantener los elementos ordenados y se desea reducir la complejidad temporal 
        de las operaciones en el árbol. Por ejemplo, se puede utilizar en bases de datos para almacenar y ordenar registros, en motores de 
        búsqueda para indexar y clasificar resultados, en compiladores para optimizar el análisis sintáctico y semántico, y en muchas 
        otras aplicaciones.[6]'''
    )
    codeAVLtree()
    impAVL()

def rojo_negro():
    """Visualización de información de los árboles rojo negro, junto con su implementación interactiva"""
    st.header('Árboles rojo negro')
    st.write(
        '''
        Son una estructura de datos basada en árboles binarios de búsqueda que se utiliza para mantener los elementos de 
        manera ordenada y equilibrada. Estos árboles se llaman así debido a las propiedades de sus nodos, que son etiquetados 
        como "rojos" o "negros"[6].
        '''
    )
    st.subheader('Características')
    st.markdown(
        '''
        - Cada nodo es etiquetado como rojo o negro.
        - La raíz del árbol siempre es de color negro.
        - Todos los nodos hoja (nodos nulos o NIL) son considerados negros.
        - Si un nodo es rojo, entonces sus hijos deben ser negros.
        - Cada camino desde un nodo hasta sus nodos descendientes contiene la misma cantidad de nodos negros. Esto se conoce 
        como la "propiedad del número de nodos negros".
        - El camino más largo es dos veces el camino mas corto.
        - Todo nodo que se inserta es rojo.
        '''
    )
    st.write(
        '''
        Estas reglas garantizan que un árbol rojo-negro esté equilibrado y tenga una altura logarítmica, lo que resulta en un 
        tiempo de ejecución eficiente para operaciones de búsqueda, inserción y eliminación.'''
    )
    st.subheader('_Inserción_')
    insertar_nodos_rbTree()

def tipos():
    """Visualización de los tipos de árboles"""
    st.header('Tipos de árboles')
    tipos_arboles = ['Árbol n-ario', 'Árbol binario', 'Árboles binarios de búsqueda', 'Árboles de búsqueda avanzados (AVL)', 'Árboles rojo negro']
    n_ario, binario, binario_busqueda, avl, arbol_rojo_negro = st.tabs(tipos_arboles)
    with n_ario:
        n_arios()
    with binario:
        binarios()
        reglas_binarios()
        code_binary_tree()
    with binario_busqueda:
        binarios_busqueda()
    with avl:
        arbolesAVL()
    with arbol_rojo_negro:
        rojo_negro()
    
def ejercicios_basicos():
    """Visualización de los ejercicios básicos de implementación"""
    st.header("Ejercicios")
    st.write("""A continuación te mostraremos ejercicios para que apliques lo aprendido, la solución se muestra una vez indiques en el botón
            que quieres verla, sin embargo te recomendamos que intentes resolverlo tu solo para tu mejor comprensión. Recuerda que la mejor manera de 
            aprender es haciéndolo tu mismo.""")
    ejercicio1()
    ejercicio2()
    ejercicio3()

def page():
    """Organización de la página árboles"""
    intro()
    opcion = st.selectbox(
        'Escoge el tema a desplegar',
        (
            '',
            'Definiciones importantes',
            'Tipos de árboles',
            'Ejercicios básicos de comprensión',
            'Ejercicio de aplicación'
        )
    )
    if opcion == 'Definiciones importantes':
        importante_saber()
        tabs()
    elif opcion == 'Tipos de árboles':
        tipos()
    elif opcion == 'Ejercicios básicos de comprensión':
        ejercicios_basicos()
    elif opcion == 'Ejercicio de aplicación':
        mostrar_prediccion()

page()

