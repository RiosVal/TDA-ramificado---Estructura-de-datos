from codigos.arboles.huffman import codificar_huffman, decodificar_huffman
import streamlit as st

def uso_huffman():
    """Aplicación del código de Huffman
    """
    datos = st.text_input('Ingresa texto a codificar')
    datos_codificados, arbol = codificar_huffman(datos)
    datos_decodificados = decodificar_huffman(datos_codificados, arbol)
    st.write("Mensaje original:", datos)
    st.write("Mensaje codificado:", datos_codificados)
    st.write("Mensaje decodificado:", datos_decodificados)
