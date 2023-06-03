import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Bienvenido a TDA's learning")

Arboles = "Árboles"
Grafos = "Grafos"
Monticulos ="Monticulos"

option = st.selectbox(
    "Escoge el tema que quieres aprender",
    ('-', Arboles, Grafos,Monticulos)
)

if st.button("Enviar"):
    if option == Arboles:
        switch_page("Arboles")
    if option == Grafos:
        switch_page("Grafos")
    if option == Monticulos:
        switch_page("Monticulos")
