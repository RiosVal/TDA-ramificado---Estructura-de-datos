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
            - Teoría de grafos - UniPamplona (2015). Estructura de Datos : Grafos y vertices [online]. Available: https://www.youtube.com/watch?v=tbCw6pq1E7c&list=PLCh9J2_B_crLJN8L_1aVfJL-kjfEiazvv&index=2
            - Algoritmo de Dijkstra - Wikipedia (2004). Estructura de Datos : Dijkstra [online]. Available:https://es.wikipedia.org/wiki/Algoritmo_de_Dijkstra
        '''
    )

def referencias_monticulos():
    st.header('Montículos')
    st.markdown(
        '''
            - "TDA ramificado", class notes for 79021-3L- 1195 - 1587 Estructura de datos, Facultad de ingeniería, Universidad de San Buenaventura Cali, 2023
            - [1]vestigium [Online]. Available: https://www.glc.us.es/~jalonso/vestigium/i1m2018-ejercicios-con-el-tipo-abstracto-de-dato-de-los-monticulos/ 
            - [2]Tema5.3_ColasPrioridad_Monticulos[EDA][online]. Available: https://www.cartagena99.com/recursos/alumnos/apuntes/Tema5.3_ColasPrioridad_Monticulos[EDA].pdf
            - [3]udb.edu.co[online]. Available: https://www.udb.edu.sv/udb_files/recursos_guias/informatica-ingenieria/programacion-con-estructuras-de-datos/2019/i/guia-9.pdf
            - [4]Monticulos.pdf [online]. Available: file:///C:/Users/jcast/Downloads/Monti.pdf
        '''
    )

def page():
    st.title('📖')
    st.title('Referencias')
    referencias_arboles()
    referencias_grafos()
    referencias_monticulos()

page()