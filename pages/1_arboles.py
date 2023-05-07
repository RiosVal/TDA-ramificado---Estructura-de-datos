import streamlit as st
from codigos.arboles import *

st.header("🌳")
st.markdown('<h1>Árboles</h1>', unsafe_allow_html=True)
st.markdown(
    """
        <p>
            Los árboles son estructuras de datos que se caracterizan por almacenar sus nodos en forma jerárquica, a diferencia de las listas
            que los almacenan en forma lineal.
        </p>
    """,
    unsafe_allow_html=True
)

st.markdown("<h2>Importante entender</h2>", unsafe_allow_html=True)
st.markdown(
    """<p>Los árboles se componen de los siguientes elementos:</p>""", unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("- <b>Nodos:</b> son todos los elementos que tiene un árbol", unsafe_allow_html=True)
    st.markdown("- <b>Raíz:</b> primer nodo del árbol, es único", unsafe_allow_html=True)
    st.markdown("- <b>Padre:</b> son todos los nodos que tienen al menos un hijo", unsafe_allow_html=True)
with col2:
    st.markdown("- <b>Hijo:</b> son todos los nodos que tienen un padre", unsafe_allow_html=True)
    st.markdown("- <b>Hermano:</b> son aquellos nodos que comparten un mismo padre", unsafe_allow_html=True)
    st.markdown("- <b>Hoja:</b> nodos que no tienen hijos", unsafe_allow_html=True)
with col3:
    st.markdown("- <b>Rama:</b> aquellos nodos que no son la raíz y tienen al menos un hijo", unsafe_allow_html=True)
    st.markdown("- <b>Nivel:</b> cada generación dentro del árbol es un nivel", unsafe_allow_html=True)
    st.markdown("- <b>Altura:</b> número máximo de niveles en un árbol", unsafe_allow_html=True)
with col4:
    st.markdown("- <b>Peso:</b> número de nodos que tiene un árbol", unsafe_allow_html=True)
    st.markdown("- <b>Orden:</b> número máximo de hijos que puede tener un nodo", unsafe_allow_html=True)
    st.markdown("- <b>Grado:</b> número mayor de hijos que tiene alguno de los nodos del Árbol", unsafe_allow_html=True)


tab1, tab2, tab3, tab4 = st.tabs(["Árbol", "Raíz, rama, hoja", "Nodos padre e hijos", "Hermanos"])

with tab1:
    st.image("images/arboles/arbol.png")
with tab2:
    st.image("images/arboles/padreHermanos.png")
with tab3:
    st.image("images/arboles/padreHijo.png")
with tab4:
    st.image("images/arboles/RaizRamaHoja.png")

col11, col21 = st.columns(2)

with col11:
    st.markdown("<h2>Árbol n-ario</h2>", unsafe_allow_html=True)
    st.markdown("Aquellos arboles donde el número máximo de hijos por nodo es de N.", unsafe_allow_html=True)
with col21:
    st.markdown("<h2>Árbol binario</h2>", unsafe_allow_html=True)
    st.markdown("Árbol n-ario de Grado 2, cada nodo solo puede tener máximo 2 hijos.", unsafe_allow_html=True)

st.divider()
st.header("En estructura de datos se utilizan árboles binarios")
st.subheader("Reglas")
st.markdown(
    """
        - Siempre va a haber un nodo raiz
        - Los datos menores o iguales a la raíz van a la izquierda
        - Los datos mayores van a la derecha de la raíz
    """
)

code_binary_tree()

st.divider()
st.header("Ejercicios")
st.write("""A continuación te mostraremos ejercicios para que apliques lo aprendido, la solución se muestra una vez indiques en el botón
        que quieres verla, sin embargo te recomendamos que intentes resolverlo tu solo para tu mejor comprensión. Recuerda que la mejor manera de 
        aprender es haciéndolo tu mismo.""")

ejercicio1()
ejercicio2()
ejercicio3()