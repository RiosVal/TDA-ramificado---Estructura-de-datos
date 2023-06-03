import streamlit as st
from sklearn import tree
import matplotlib.pyplot as plt




def code_prediccion():
    st.subheader("Actividad")
    opcion = st.selectbox(
        '''Implementar un algoritmo que permita generar un árbol de decisión meteorológico para la 
        predicción
        del estado del tiempo basado en las reglas de la
        siguiente figura''',
        ("-", "Mostrar solución")
    )
    if opcion == "Mostrar solución":
        code = '''class NodoArbol:
    def __init__(self, variable, valor_umbral, nodo_izquierdo, nodo_derecho):
        self.variable = variable
        self.valor_umbral = valor_umbral
        self.nodo_izquierdo = nodo_izquierdo
        self.nodo_derecho = nodo_derecho


def predecir_estado_tiempo(registro, raiz):
    nodo_actual = raiz

    while nodo_actual.nodo_izquierdo:
        if registro[nodo_actual.variable] <= nodo_actual.valor_umbral:
            nodo_actual = nodo_actual.nodo_izquierdo
        else:
            nodo_actual = nodo_actual.nodo_derecho

    return nodo_actual.variable
'''
        st.code(code, language='python')













# Definir los datos de entrenamiento
datos_entrenamiento = [[30, 70, 10],
                       [25, 80, 5],
                       [20, 90, 15],
                       [15, 95, 5],
                       [35, 50, 20]]
etiquetas = ['despejado', 'parcialmente nublado', 'mayormente nublado', 'nublado', 'lluvia']

# Crear un clasificador de árbol de decisión
clf = tree.DecisionTreeClassifier()

# Entrenar el clasificador con los datos de entrenamiento
clf.fit(datos_entrenamiento, etiquetas)

# Interfaz de Streamlit en tu página web
def mostrar_prediccion():
    temperatura = st.number_input("Temperatura (°C):", min_value=-100.0, max_value=100.0)
    humedad = st.number_input("Humedad (%):", min_value=0.0, max_value=100.0)
    velocidad_viento = st.number_input("Velocidad del Viento (km/h):", min_value=0.0)

    nuevas_caracteristicas = [[temperatura, humedad, velocidad_viento]]

    if st.button("Mostrar resultados"):
        resultado = clf.predict(nuevas_caracteristicas)
        st.write("La predicción del estado del tiempo es:", resultado[0])

        # Generar gráfico del árbol de decisión
        fig, ax = plt.subplots(figsize=(8, 6))
        tree.plot_tree(clf, feature_names=["Temperatura", "Humedad", "Velocidad Viento"], class_names=etiquetas, filled=True, ax=ax)
        st.pyplot(fig)

# Llamar a la función para mostrar la predicción en tu página web
mostrar_prediccion()
