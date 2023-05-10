import streamlit as st

st.header("🕸️")
st.markdown('<h1>Grafos</h1>', unsafe_allow_html=True)
st.markdown(
    """
        <p>
            Un grafo es una estructura de datos no lineal que consta de vértices y aristas. Los vértices a veces también se denominan nodos y los bordes son líneas o arcos que conectan dos nodos en el grafo. Más formalmente, un grafo se compone de un conjunto de vértices (V) y un conjunto de aristas (E). El grafo se denota por G(E, V).

        </p>


""", unsafe_allow_html=True)

st.markdown("<h2> Importante entender </h2>", unsafe_allow_html=True)
st.markdown(
    """
    
        <p> Los Grafos se componen por los siguientes elementos:   </p>
    
    """
, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1: 
    st.markdown("- <b> Vertices:</b> son las unidades fundamentales del grafo. A veces, los vértices también se conocen como vértices o nodos. Cada nodo/vértice se puede etiquetar o no etiquetar.", unsafe_allow_html=True)

with col2:
    st.markdown("- <b> Aristas: Las aristas se dibujan o se usan para conectar dos nodos del gráfico. Se puede ordenar un par de nodos en un gráfico dirigido. Las aristas pueden conectar dos nodos cualesquiera de cualquier forma posible. Las aristas también se conocen como arcos. Cada arista se puede etiquetar/desetiquetar. </b>",unsafe_allow_html=True)


tab1,tab2,tab3,tab4,tab5 = st.tabs(["Grafos no dirigidos","Grafos dirigidos","Grafos Ponderado","Grafos No Ponderado","Grafos Completos"])

with tab1: #GRAFOS NO DIRIGIDOS
    #   st.image()
    st.markdown("""

    <p> Un grafo en el que los bordes no tienen dirección, es decir, los bordes no tienen flechas que indiquen la dirección de recorrido. Ejemplo: un grafo de red social donde las amistades no son direccionales.</p>

    """,unsafe_allow_html=True)
with tab2: #GRAFOS DIRIGIDOS
    #st.image()
    st.markdown("""

    <p> Un grafo en el que los bordes tienen una dirección, es decir, los bordes tienen flechas que indican la dirección de recorrido. Ejemplo: un grafo de página web donde los enlaces entre páginas son direccionales. </p>

    """,unsafe_allow_html=True)
with tab3: #GRAFOS PONDERADOS
    #st.image()
    st.markdown("""

    <p> Un grafo en el que los bordes tienen pesos o costos asociados con ellos. Ejemplo: un grafo de red de carreteras donde los pesos pueden representar la distancia entre dos ciudades. </p>

    """,unsafe_allow_html=True)
with tab4: #GRAFOS NO PONDERADOS
    #st.image()
    st.markdown("""

    <p> 
Un grafo en el que los bordes no tienen pesos ni costes asociados. Ejemplo: un grafo de red social donde los bordes representan amistades.</p>

    """,unsafe_allow_html=True)
with tab5: #GRAFOS COMPLETOS
    #st.image()
    st.markdown("""

    <p> Un grafo en el que cada vértice está conectado a todos los demás vértices. Ejemplo: un grafo de torneo donde cada jugador juega contra todos los demás jugadores</p>

    """,unsafe_allow_html=True)


tab6,tab7,tab8,tab9,tab10 = st.tabs(["Grafos Bipartitos","Arboles","Ciclos","Grafos Dispersos","Grafos Densos"])

with tab6: #GRAFOS BIPARTITOS
    #st.image()
    st.markdown("""

    <p> </p>

    """)
with tab7: #GRAFOS (ARBOLES)
    #st.image()
    st.markdown("""

    <p> </p>

    """)
with tab8: #CICLOS
   # st.image()
    st.markdown("""

    <p> </p>

    """)
with tab9: #GRAFOS DISPERSOS
   # st.image()
    st.markdown("""

    <p> </p>

    """)
with tab10: #GRAFOS 
   # st.image()
    st.markdown("""

    <p> </p>

    """)
