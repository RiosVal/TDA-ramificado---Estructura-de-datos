import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.markdown("<h1>Bienvenido a TDA's learning</h1>", unsafe_allow_html=True)

arboles = "Árboles"
grafos = "Grafos"

option = st.selectbox(
    "Escoge el tema que quieres aprender",
    ('-', arboles, grafos)
)

if st.button("Enviar"):
    if option == arboles:
        switch_page("arboles")