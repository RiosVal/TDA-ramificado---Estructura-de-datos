""" 
Priorizar el aterrizaje y despege de los aviones de la fuerza aerea
"""
import streamlit as st
import time
from codigos.monticulos.TDA_Monticulos import TdaMonticulo

aterrizaje_monticulo = TdaMonticulo(10)
despegue_monticulo = TdaMonticulo(10)

def ingresar_avion():

    tipo_input = st.empty()  # Referencia al widget de entrada de tipo
    prioridad_input = st.empty()  # Referencia al widget de entrada de prioridad
    
    opcion = st.selectbox("Seleccionar acción:", ["Aterrizaje", "Despegue"])
    tipo = tipo_input.text_input("Tipo de avión:", value="")
    prioridad = prioridad_input.number_input("Prioridad:", 0, 100, 0, 1)
    confirmado = st.button("Agregar avión")
    
    if confirmado:
        
        if opcion == "Aterrizaje":
            aterrizaje_monticulo.agregar((prioridad, tipo))
        else:
            despegue_monticulo.agregar((prioridad, tipo))
        
        mensaje_exito = st.empty()
        mensaje_exito.success("Avión agregado correctamente")
        time.sleep(2)  # Tiempo de espera para mostrar el mensaje
        mensaje_exito.empty()  # Eliminar el mensaje de éxito


def imprimir_lista():
    st.subheader("Lista de aviones organizada según prioridad de aterrizaje:")
    aterrizaje_monticulo.imprimir_heap_streamlit()

    st.subheader("Lista de aviones organizada según prioridad de despegue:")
    despegue_monticulo.imprimir_heap_streamlit()


def menu_ejercicio_aplicativo():
    st.title("Gestión de aviones")
    
    opcion = st.selectbox("Seleccionar acción:", ["", "Ingresar avion", "Imprimir lista"])
    
    if opcion == "Ingresar avion":
        ingresar_avion()
    elif opcion == "Imprimir lista":
        imprimir_lista()