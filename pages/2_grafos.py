import streamlit as st
from codigos.grafos.grafos_dij import *
from codigos.grafos.grafos import *
from codigos.grafos.rbGraphs import *
from codigos.grafos.grafos_eje import *
from codigos.grafos.grafos_matriz import *



def intro():
    st.header("🕸️")

    st.markdown('<h1>Grafos</h1>', unsafe_allow_html=True)
    st.markdown(
        """
          <p>
             Un grafo es una estructura de datos no lineal que consta de vértices y aristas.
             Los vértices a veces también se denominan nodos y los bordes son líneas o arcos que conectan dos nodos en el grafo. 
             Más formalmente, 
             un grafo se compone de un conjunto de vértices 
             (V) y un conjunto de aristas (E). El grafo se denota por G(E, V).

         </p>


    """, unsafe_allow_html=True)

def importante_saber():
    st.markdown("<h2> Importante entender </h2>", unsafe_allow_html=True)
    st.markdown("""<p> Los Grafos se componen por los siguientes elementos:</p>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # with col1: 
    #     st.markdown("- <b> Vertices:</b> son las unidades fundamentales del grafo. A veces, los vértices también se conocen como vértices o nodos. Cada nodo/vértice se puede etiquetar o no etiquetar.", unsafe_allow_html=True)
    #     st.markdown("- <b> Adyacencia: </b> ", unsafe_allow_html=True)
    with col1:
        st.markdown("- <b> Vertices:</b> son las unidades fundamentales del grafo. A veces, los vértices también se conocen como vértices o nodos. Cada nodo/vértice se puede etiquetar o no etiquetar.", unsafe_allow_html=True)
        st.markdown("- <b>Adyacencia:</b> Representa una lista de vertices ", unsafe_allow_html=True)
        st.markdown("- <b>Camino:</b> Es una secuencia de arcos, la cual cada extremo coincide con el inicio y el final", unsafe_allow_html=True)
        st.markdown("- <b>Longitud de camino:</b> Es el número de numero de aristas que la forman ",unsafe_allow_html=True)


    with col2:
        st.markdown("- <b> Aristas: </b> Las aristas se dibujan o se usan para conectar dos nodos del gráfico. Se puede ordenar un par de nodos en un gráfico dirigido. Las aristas pueden conectar dos nodos cualesquiera de cualquier forma posible. Las aristas también se conocen como arcos. Cada arista se puede etiquetar/desetiquetar. </b>",unsafe_allow_html=True)
        st.markdown("- <b> Etiqueta de arista:</b> son aquellos en los que las aristas tienen una etiqueta o peso asociado que representa alguna característica o propiedad específica ",unsafe_allow_html=True)
        st.markdown("- <b> Conexo:</b> todos sus vertices tine una relacion o una forma de comunicarse entre si ya se simple o relacionandose a traves de uno a más aristas",unsafe_allow_html=True)
    st.image("images/grafos/partes grafos.png")
def tabs():
    tab1,tab2,tab3,tab4,tab5,tab6= st.tabs(["Grafos no dirigidos","Grafos dirigidos"," Camino hamiltoneano","Camino euleriano","Grafos aciclico","Grafos ponderados"])

    with tab1: #GRAFOS NO DIRIGIDOS
        #   st.image()
        st.markdown("""

        <p> Un grafo en el que los bordes no tienen dirección, es decir, los bordes no tienen flechas que indiquen la dirección de recorrido. Ejemplo: un grafo de red social donde las amistades no son direccionales.</p>

        """,unsafe_allow_html=True)
        st.image("images/grafos/g.no dirigidos.png")
    with tab2: #GRAFOS DIRIGIDOS
        #st.image()
        st.markdown("""

     <p> Un grafo en el que los bordes tienen una dirección, es decir, los bordes tienen flechas que indican la dirección de recorrido. Ejemplo: un grafo de página web donde los enlaces entre páginas son direccionales. </p>

        """,unsafe_allow_html=True)
        st.image("images/grafos/g.dirigidos.png")
    with tab3: #Camino hamiltoneano
        #st.image()
        st.markdown("""

            <p>En el campo matemático de la teoría de grafos, es un camino
            de un grafo, una sucesión de aristas adyacentes, que visita
            todos los vértices del grafo una sola vez. Si además el último
            vértice visitado es adyacent al primero, el camino es un ciclo
            hamiltoniano.</p>
         """,unsafe_allow_html=True)
        st.image("images/grafos/hamiltoniano.png")
    with tab4: #camino euleriano
        #st.image()
        st.markdown("""

        <p> Un ciclo euleriano es un Camino en un grafo que
        comienza y termina en el mismgvértice, que incluye
        cada arista del grafo exactamente una vez y que
        puede tener vértices repetidos, es decir, un ciclo que
        incluye todas las aristas y que estas no se repitan.
        .</p>

        """,unsafe_allow_html=True)
        st.image("images/grafos/euleriano.png")
    with tab5: #GRAFOS aciclico
        #st.image()
        st.markdown("""

        <p>es aquel en el que no hay ciclos, lo que significa que no se puede seguir una secuencia de aristas y nodos que forme un camino cerrado. En un grafo acíclico, los caminos siempre van en una dirección, lo que hace que su estructura sea más simple y fácil de analizar..</p>

        """,unsafe_allow_html=True)
        st.image("images/grafos/aciclico.png")
    with tab6: #Grafos ponderados
        st.markdown("""

        <p>Un grafo ponderado es una estructura de datos que consiste en un conjunto de vértices o nodos interconectados mediante aristas o arcos, donde cada arista tiene asignado un valor numérico conocido como peso o costo. Estos pesos representan la medida de la distancia, costo, tiempo u otra propiedad asociada a la conexión entre los nodos.
        </p>

        """,unsafe_allow_html=True)
        st.image("images/grafos/grafos ponderados.png")    


def  usos_reglas():
    st.subheader("Usos")
    st.markdown(
    """
    -Representación de redes: Los grafos se utilizan para representar redes de computadoras, sistemas de comunicación y redes sociales. Los nodos del grafo representan los elementos de la red, como routers, servidores, usuarios, etc. Las aristas del grafo representan las conexiones entre los nodos, como cables, enrutadores, conexiones de red, etc.

    -Análisis de algoritmos: Los grafos se utilizan para analizar el rendimiento de los algoritmos. Por ejemplo, se puede representar el flujo de datos y el costo de las operaciones en un algoritmo mediante un grafo. Luego, se pueden aplicar técnicas de análisis de grafos para optimizar el algoritmo y mejorar su rendimiento.

    -Optimización de rutas: Los grafos se utilizan para encontrar la mejor ruta entre dos puntos en una red. Por ejemplo, se puede utilizar un algoritmo de búsqueda en grafos para encontrar la ruta más corta entre dos ciudades en un mapa.

    -Minería de datos: Los grafos se utilizan para modelar y analizar datos complejos, como redes sociales, sistemas de recomendación y patrones de tráfico en la web. Los grafos pueden utilizarse para identificar comunidades, nodos influyentes y patrones de comportamiento en grandes conjuntos de datos.

    -Modelado de sistemas: Los grafos se utilizan para modelar sistemas complejos, como sistemas de control de procesos industriales, sistemas de transporte, sistemas de energía eléctrica, etc. Los grafos se utilizan para representar los componentes del sistema, las interacciones entre ellos y las restricciones y objetivos del sistema.
    """
    )

    st.divider()
    st.header("En estructura de datos se utilizan  los grafos, y existen unas reglas:")
    st.subheader("Reglas")
    st.markdown(
    """
        - Definir los nodos y aristas: Primero, debes definir los nodos o vértices del grafo, así como las aristas o conexiones entre ellos. Puedes asignar identificadores únicos a cada nodo para facilitar su referencia.
        - Elegir una estructura de datos adecuada: Selecciona una estructura de datos que se ajuste a tus necesidades y al tipo de operaciones que planeas realizar con el grafo. Las opciones comunes son la matriz de adyacencia y la lista de adyacencia, como se mencionó anteriormente.
        - Implementar funciones básicas: Debes implementar funciones básicas para trabajar con grafos, como agregar un nodo, agregar una arista, eliminar un nodo, eliminar una arista, buscar nodos adyacentes, etc. Estas funciones variarán según la estructura de datos que estés utilizando.
        - Considerar la dirección de las aristas: Puedes optar por trabajar con un grafo dirigido (las aristas tienen una dirección) o un grafo no dirigido (las aristas no tienen dirección). Esta elección afectará la forma en que almacenas y procesas las aristas.
        - Manejar la conectividad: Asegúrate de manejar adecuadamente la conectividad del grafo. Esto implica garantizar que no haya nodos o aristas duplicados, y que los nodos estén correctamente conectados entre sí.
        - Implementar algoritmos y operaciones: Puedes aplicar algoritmos y operaciones específicas a los grafos según tus necesidades, como búsqueda en profundidad, búsqueda en amplitud, algoritmos de recorrido, algoritmos de búsqueda de caminos más cortos, algoritmos de árbol de expansión mínima, entre otros.
    """
    )


def definciones():
    st.header("Adyacencia")
    st.markdown(
     """
    La adyacencia en grafos se refiere a la relación entre dos nodos o vértices que están conectados por una arista. Dos nodos se consideran adyacentes si existe una arista que los conecta. En otras palabras, la adyacencia indica que dos nodos están directamente conectados en un grafo. La adyacencia puede ser bidireccional o unidireccional, dependiendo de si las aristas tienen una dirección o no. La información sobre la adyacencia de los nodos en un grafo es fundamental para realizar operaciones y análisis sobre el mismo, como encontrar rutas, determinar la conectividad o calcular distancias entre nodos.
    """
    )
    #posible imagen


    st.divider()
    st.header("Caminos & longitud de un camino")
    st.markdown(
    """
     un camino es una secuencia de nodos conectados en el que cada par de nodos consecutivos está unido por una arista. En otras palabras, es una ruta que permite ir desde un nodo inicial a un nodo final pasando por una serie de nodos intermedios, siguiendo las conexiones del grafo.

    Un camino puede ser de longitud cero si se trata de un solo nodo, y puede ser de longitud uno si hay una arista directa entre dos nodos. La longitud de un camino se mide por el número de aristas que contiene.

    Los caminos en los grafos son utilizados para analizar la conectividad entre nodos, encontrar rutas más cortas entre dos nodos específicos, determinar si existe un camino entre dos nodos, o identificar componentes conectados dentro de un grafo.

    Existen diferentes tipos de caminos en grafos, como el camino simple (no se repiten nodos en el camino), el camino cíclico (donde el nodo inicial y final son el mismo), y el camino ponderado (donde cada arista tiene asignado un peso o costo).

    El estudio y análisis de los caminos en grafos es fundamental en la teoría de grafos y es aplicado en diversos campos, como redes de comunicación, algoritmos de navegación, análisis de redes sociales, optimización de rutas, entre otros.
    """
    )

    st.image("images/grafos/Camino.png")

    st.divider()
    st.header("Etiqueta de una arista")
    st.markdown(
    """
    En el contexto de los grafos, una etiqueta de arista se refiere a un valor o atributo asociado a una arista específica. Es una información adicional que se puede asignar a una arista para representar alguna característica o propiedad relacionada con la conexión que representa. Estas etiquetas pueden ser numéricas, de texto o incluso estructuras de datos más complejas, dependiendo de las necesidades específicas del problema que se esté abordando. Las etiquetas de arista son útiles para representar información como el peso de una conexión, el costo de atravesar una arista, el tipo de relación entre dos nodos o cualquier otra información relevante para el grafo en cuestión.
    """
    )
    #posible imagen
    st.image("images/grafos/Etiquetas.png")

    st.divider()
    st.header("conexo")
    st.markdown(
    """
    En un grafo, se dice que es conexo si existe un camino entre cualquier par de nodos del grafo. En otras palabras, todos los nodos del grafo están conectados entre sí de alguna manera. Si hay al menos un par de nodos que no están conectados por ningún camino, entonces el grafo se considera no conexo. En un grafo no dirigido, la noción de conexidad implica que la relación de conexión es simétrica, es decir, si el nodo A está conectado con el nodo B, entonces el nodo B también está conectado con el nodo A.
    """
    )   

    st.divider()
    st.header("grafo dirigido y  grafo no dirigido")
    st.markdown(
    """
        -Grafo dirigido: Un grafo dirigido, también conocido como digrafo, es un tipo de grafo donde las aristas tienen una dirección asociada. Esto significa que la conexión entre dos nodos va en una dirección específica, lo que implica que se puede viajar desde un nodo inicial a un nodo final siguiendo la dirección de las aristas. En un grafo dirigido, las aristas se representan con flechas o arcos para indicar la dirección.
        
        -Grafo no dirigido: Un grafo no dirigido es un tipo de grafo donde las aristas no tienen una dirección asociada. En otras palabras, la conexión entre dos nodos es bidireccional, lo que significa que se puede viajar en ambas direcciones entre los nodos sin restricciones. En un grafo no dirigido, las aristas se representan con líneas sin flechas para indicar que la conexión es simétrica.
    """
    )
    st.subheader("conclusiones")
    st.markdown(
    """la principal diferencia entre un grafo dirigido y un grafo no dirigido radica en la dirección de las aristas: en un grafo dirigido, las aristas tienen una dirección específica, mientras que en un grafo no dirigido, las aristas no tienen dirección y la conexión es bidireccional.
    """
    )

def codigos():
    code_grafos()

def dijkstra():
    cod_dijkstra()
    

def adye():
    in_adya()

def vec():
    in_vec()

def matriz():    
    in_matriz()


def ejercicios_basicos():
    st.subheader("Ejercicio")
    st.markdown(
    """
    A continuación, te mostraremos ejercicios para que apliques lo aprendido, la solución se muestra una vez indiques en el botón
            que quieres verla, sin embargo, te recomendamos que intentes resolverlo tu solo para tu mejor comprensión. Recuerda que la mejor manera de 
            aprender es haciéndolo tú mismo.
    """
    )
    ejercicio1()
    graficar_comunicacion_redes()
    ejercicio2()
    encontrar_camino_mas_corto()
    ejercicio3()
    encontrar_componentes_conectados()

def page():
    #menu donde el  usrauario podra ver los temas y codigos que tiene que ver con un grafo#
    """Organización de la página árboles"""
    intro()
    opcion = st.selectbox(
        'Escoge el tema  desplegar',
        (
            '',
            'Definiciones importantes',
            'Usos y reglas',
            'Información detallada',
            'Codigo de los grafos',
            'Codigo de dijkstra',
            'Codigo de matriz de adyacencia',
            'Codigo de matriz de vectores',
            'Codigo de matriz de lista',
            'Ejercicios básicos de comprensión'
        )
    )
    #opciones delm menu
    if opcion == 'Definiciones importantes':
        importante_saber()
        tabs()
    elif opcion == 'Usos y reglas':
        usos_reglas()
    elif opcion == 'Información detallada':
        definciones()
    elif opcion == 'Codigo de los grafos':
        codigos()
    elif opcion == 'Codigo de dijkstra':
        dijkstra()
    elif opcion == 'Codigo de matriz de adyacencia':
        adye()
    elif opcion == 'Codigo de matriz de vectores':
        vec()
    elif opcion == 'Codigo de matriz de lista':
        matriz()
    elif opcion == 'Ejercicios básicos de comprensión':
        ejercicios_basicos()
page()
