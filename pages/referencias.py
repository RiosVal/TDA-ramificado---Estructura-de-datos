import streamlit as st


def referencias_arboles():
    st.header('Árboles')
    st.markdown(
        '''
            - "TDA ramificado", class notes for 79021-3L- 1195 - 1587 Estructura de datos, Facultad de ingeniería, Universidad de San Buenaventura Cali, 2023
            - (8 de mayo 2023). Binary Tree Data Structure [online]. Available: https://www.geeksforgeeks.org/binary-tree-data-structure/
            - O. Blancarte (22 de agosto 2014). Estructura de datos – Árboles [online]. Available: https://www.oscarblancarteblog.com/2014/08/22/estructura-de-datos-arboles/
            - C. Ramos (18 de agosto 2016). 27 Estructura de Datos : Arbol Binario parte 3:4 Python 3.5 [online]. Available: https://www.youtube.com/watch?v=tbCw6pq1E7c&list=PLCh9J2_B_crLJN8L_1aVfJL-kjfEiazvv&index=2
            - M.A. Bañolas Adrogué, "Estructura de datos avanzadas : clases disjuntas, montículos, árboles de búsqueda", Bachelor Thesis, Universitat Oberta de Catalunya, Catalunya España, 2010
        '''
    )

def referencias_grafos():
    st.header('Grafos')
    st.markdown(
        '''
            - "TDA ramificado", class notes for 79021-3L- 1195 - 1587 Estructura de datos, Facultad de ingeniería, Universidad de San Buenaventura Cali, 2023

        '''
    )

def referencias_monticulos():
    st.header('Montículos')
    st.markdown(
        '''
            - "TDA ramificado", class notes for 79021-3L- 1195 - 1587 Estructura de datos, Facultad de ingeniería, Universidad de San Buenaventura Cali, 2023

        '''
    )

def page():
    st.title('📖')
    st.title('Referencias')
    referencias_arboles()
    referencias_grafos()
    referencias_monticulos()
