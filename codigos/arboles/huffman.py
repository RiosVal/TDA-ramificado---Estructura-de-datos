from heapq import heappush, heappop, heapify
from collections import defaultdict

# Función auxiliar para crear un árbol de Huffman
def construir_arbol_huffman(freq):
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

# Función para codificar el mensaje
def codificar_huffman(datos):
    freq = defaultdict(int)
    for char in datos:
        freq[char] += 1
    if not freq:
        return "", None
    arbol_huff = construir_arbol_huffman(freq)
    huff_dict = {char: code for char, code in arbol_huff}
    encoded = "".join(huff_dict[char] for char in datos)
    return encoded, arbol_huff

# Función para decodificar el mensaje
def decodificar_huffman(datos_codificados, arbol_huff):
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
