from heapq import heappush, heappop, heapify
from collections import defaultdict

def construir_arbol_huffman(freq):
    """Función auxiliar para crear un árbol de Huffman

    Args:
        freq (defaultdict):  símbolos y sus frecuencias en los datos a comprimir.

    Returns:
        list: lista de pares de símbolos y códigos binarios ordenados según la longitud de los códigos.
    """
    heap = [[peso, [símbolo, ""]] for símbolo, peso in freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for par in lo[1:]:
            par[1] = '0' + par[1]
        for par in hi[1:]:
            par[1] = '1' + par[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def codificar_huffman(datos):
    """Función para codificar el mensaje

    Args:
        datos (string): string que se desea comprimir utilizando Huffman.

    Returns:
        tuple: cadena comprimida y el árbol de Huffman.
    """
    freq = defaultdict(int)
    for char in datos:
        freq[char] += 1
    if not freq:
        return "", None
    arbol_huff = construir_arbol_huffman(freq)
    huff_dict = {char: code for char, code in arbol_huff}
    encoded = "".join(huff_dict[char] for char in datos)
    return encoded, arbol_huff


def decodificar_huffman(datos_codificados, arbol_huff):
    """Función para decodificar el mensaje

    Args:
        datos_codificados (string): string codificado
        arbol_huff (arbol de huffman):  el árbol de Huffman

    Returns:
        string: cadena decodificada
    """
    if not arbol_huff:
        return ""
    dec_dict = {code: char for char, code in arbol_huff}
    codigo_actual = ""
    decoded = ""
    for bit in datos_codificados:
        codigo_actual += bit
        if codigo_actual in dec_dict:
            decoded += dec_dict[codigo_actual]
            codigo_actual = ""
    return decoded
