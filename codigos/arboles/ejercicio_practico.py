import streamlit as st
from sklearn import tree

def predecir_estado_tiempo(clf, nuevas_caracteristicas):
    # Realizar la predicción basada en las nuevas características
    predicciones = clf.predict(nuevas_caracteristicas)
    
    return predicciones

# Interfaz de Streamlit en tu página web
def mostrar_prediccion():
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
    temperatura = st.number_input("Temperatura (°C):", min_value=-100.0, max_value=100.0)
    humedad = st.number_input("Humedad (%):", min_value=0.0, max_value=100.0)
    velocidad_viento = st.number_input("Velocidad del Viento (km/h):", min_value=0.0)

    nuevas_caracteristicas = [[temperatura, humedad, velocidad_viento]]

    if st.button("Mostrar resultados"):
        resultado = predecir_estado_tiempo(clf, nuevas_caracteristicas)
        st.write("La predicción del estado del tiempo es:", resultado[0])

        estructura_arbol = tree.export_text(clf, feature_names=["Temperatura", "Humedad", "Velocidad Viento"])
        st.write("Estructura del árbol de decisión:")
        st.code(estructura_arbol)

'''# Llamar a la función para mostrar la predicción en tu página web
mostrar_prediccion()'''