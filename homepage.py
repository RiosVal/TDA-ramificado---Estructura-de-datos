import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Bienvenido a TDA's learning")

arboles = "Árboles"
grafos = "Grafos"

option = st.selectbox(
    "Escoge el tema que quieres aprender",
    ('-', arboles, grafos)
)

if st.button("Enviar"):
    if option == arboles:
        switch_page("arboles")
    if option == grafos:
        switch_page("grafos")
