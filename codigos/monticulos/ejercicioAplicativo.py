import streamlit as st
from codigos.monticulos.TDA_Monticulos import Monticulo
import datetime

# Crear instancias de los montículos
monticulo_aterrizaje = Monticulo()
monticulo_despegue = Monticulo()

# Función para agregar aviones a los montículos
def agregar_avion(tipo_operacion, hora, fecha, destino, tipo_avion, referencia):
    avion = {
        'tipo_operacion': tipo_operacion,
        'hora': hora,
        'fecha': fecha,
        'destino': destino,
        'tipo_avion': tipo_avion,
        'referencia': referencia
    }
    prioridad = f"{hora}:{fecha}"
    if tipo_operacion == 'Aterrizaje':
        monticulo_aterrizaje.insertar(avion, prioridad)
    elif tipo_operacion == 'Despegue':
        monticulo_despegue.insertar(avion, prioridad)

# Función para procesar los aviones en los montículos
def procesar_aviones():
    # Generar lista priorizada de aterrizaje
    aviones_priorizados_aterrizaje = monticulo_aterrizaje.generar_lista_priorizada()
    # Generar lista priorizada de despegue
    aviones_priorizados_despegue = monticulo_despegue.generar_lista_priorizada()
    # Combinar listas priorizadas
    aviones_priorizados = aviones_priorizados_aterrizaje + aviones_priorizados_despegue
    # Ordenar la lista priorizada combinada por prioridad (hora y fecha)
    aviones_priorizados.sort(key=lambda avion: datetime.datetime.strptime(avion['hora'] + ':' + avion['fecha'], '%H:%M:%d/%m/%Y'))

    # Imprimir lista priorizada combinada
    st.subheader("Aviones Priorizados - Aterrizaje y Despegue")
    for avion in aviones_priorizados:
        tipo_operacion = avion['tipo_operacion']
        if tipo_operacion == 'Aterrizaje':
            st.write(f"ATERRIZAJE - Hora aterrizaje: {avion['hora']}, Fecha aterrizaje: {avion['fecha']}, Desde: {avion['destino']}, Tipo de avión: {avion['tipo_avion']}, Referencia: {avion['referencia']}")
        elif tipo_operacion == 'Despegue':
            st.write(f"DESPEGUE - Hora despegue: {avion['hora']}, Fecha Despegue: {avion['fecha']}, Destino: {avion['destino']}, Tipo de avión: {avion['tipo_avion']}, Referencia: {avion['referencia']}")

# Función para el menú del ejercicio aplicativo
def menu_ejercicio_aplicativo():
    st.header("Priorización de aterrizaje y despegue de aviones")

    # Formulario para agregar aviones
    st.subheader("Agregar Avión")
    tipo_operacion = st.selectbox("Tipo de operación:", ['Aterrizaje', 'Despegue'])
    referencia = st.text_input("Referencia del avión:")
    if tipo_operacion == 'Aterrizaje':
        hora = st.text_input("Hora llegada (HH : MM):")
        fecha = st.text_input("Fecha llegada (DD/MM/YYYY):")
        destino = st.text_input("Salio desde:")
    else:
        hora = st.text_input("Hora salida (HH : MM):")
        fecha = st.text_input("Fecha salida (DD/MM/YYYY):")
        destino = st.text_input("Destino:")
    tipo_avion = st.selectbox("Tipo de avión:", ["Carga", "Caza", "Transporte", "Recursos", "Emergencia", "Otro"])
    agregar = st.button("Agregar")

    if agregar:
        if tipo_operacion and hora and fecha and destino and tipo_avion and referencia:
            agregar_avion(tipo_operacion, hora, fecha, destino, tipo_avion, referencia)
            st.success("Avión agregado con éxito.")
        else:
            st.error("Por favor, complete todos los campos.")

    # Botón para procesar aviones
    st.header("Procesar Aviones")
    procesar = st.button("Procesar")

    if procesar:
        procesar_aviones()