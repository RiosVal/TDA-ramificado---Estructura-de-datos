import streamlit as st

def codeMonticulos():
    """_summary_
        Esta funcion muestra en pantalla el codigo de un monticulo en formato code y en lenguaje python
    """


    code = '''
    class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            return None
        min_value = self.heap[0]
        last_value = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last_value
            self.heapify_down(0)
        return min_value

    def get_min(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_index = index

            if (left_child_index < len(self.heap) and
                    self.heap[left_child_index] < self.heap[smallest_index]):
                smallest_index = left_child_index

            if (right_child_index < len(self.heap) and
                    self.heap[right_child_index] < self.heap[smallest_index]):
                smallest_index = right_child_index

            if smallest_index == index:
                break

            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            index = smallest_index
    '''
    st.code(code, language='python')


def codeMonticuloMax():
    """_summary_
        Esta funcion muestra en pantalla el codigo de un monticulo MAXIMO en formato code y en lenguaje python
    """

    
    code = '''
        import heapq

        class MaxHeap:
            def __init__(self):
                self.heap = []

            def insert(self, value):
                heapq.heappush(self.heap, -value)

            def extract_max(self):
                return -heapq.heappop(self.heap)

            def get_max(self):
                return -self.heap[0]

            def is_empty(self):
                return len(self.heap) == 0
        '''
    st.code(code, language='python')

def codeMonticuloMin():
    """_summary_
        Esta funcion muestra en pantalla el codigo de un monticulo MINIMO en formato code y en lenguaje python
    """

    code = '''
        import heapq

        class MinHeap:
            def __init__(self):
                self.heap = []

            def insert(self, value):
                heapq.heappush(self.heap, value)

            def extract_min(self):
                return heapq.heappop(self.heap)

            def get_min(self):
                return self.heap[0]

            def is_empty(self):
                return len(self.heap) == 0
        '''
    st.code(code, language='python')

def tda_monticulos():
    """_summary_
        Esta funcion muestra en pantalla el codigo de un TDA monticulo en formato code y en lenguaje python, tambien
        puede ser llamado por secciones
    """

    st.write("<h3>Aplicacion de TDA en monticulos:</h3>", unsafe_allow_html=True)
    st.write('''Para la aplicacion de una tda en los monticulos necesitaremos 
    un vector con n elementos que estos seran llamados <u>Heap</u> este sera util para representar un arbol binario,
    ademas usaremos funciones que definiran cada uno de su funcionamiento''',unsafe_allow_html=True)
    st.subheader("Implementacion")
    opcion = st.selectbox(
        "",
        (
            "__init__(self,tamaño)",
            "Crear_monticulo(self,tamaño)",
            "agregar(self,dato),quitar(self),flotar(self,indice)",
            "Hundir(self,indice)",
            "ordenar y revisar(self)",
            "monticulizar(self)",
            'Codigo Completo')
    )

    if opcion == "__init__(self,tamaño)":
        st.write('Crear una clase Monticulo',unsafe_allow_html=True)
        code = '''
      class Monticulo:
        def __init__(self, tamaño):
            self.heap = [None] * tamaño
            self.size = 0'''
    elif opcion == "Crear_monticulo(self,tamaño)":
        st.write('- Crea y devuelve un montículo vacío con la cantidad de elementos,determinado por el tamaño ingresado',unsafe_allow_html=True)
        code = '''
        def crear_monticulo(self, tamaño):
        self.heap = [None] * tamaño
        self.size = 0'''
    elif opcion == "agregar(self,dato),quitar(self),flotar(self,indice)":
        st.write('''- Agregar-Inserta un elemento al final del montículo y luego lo flota hasta que dicho elemento cumpla la propiedad de orden
                    - Quitar-Quita y devuelve el máximo o mínimo elemento del montículo dependiendo de su tipo, es decir el dato que se ubica en la raíz del árbol , y en su lugar se coloca 
                            el último elemento del montículo y luego lo hunde hasta que cumpla la propiedad de orden
                    - Flotar-Flota el dato almacenado en el montículo desde el índice indicado 
                            hasta que cumpla la propiedad de orden''', unsafe_allow_html=True)
        code = '''
   def agregar(self, dato):
        if self.size >= len(self.heap):
            # El montículo está lleno
            return
        self.heap[self.size] = dato
        self.flotar(self.size)
        self.size += 1

    def quitar(self):
        if self.size == 0:
            # El montículo está vacío
            return None
        dato = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.hundir(0)
        return dato

    def flotar(self, índice):
        padre = (índice - 1) // 2
        while índice > 0 and self.heap[índice] > self.heap[padre]:
            self.heap[índice], self.heap[padre] = self.heap[padre], self.heap[índice]
            índice = padre
            padre = (índice - 1) // 2'''
    elif opcion == "Hundir(self,indice)":
        st.write('- Hunde el dato almacenado en el montículo desde el índice indicado hasta que cumpla la propiedad de orden', unsafe_allow_html=True)
        code = '''
        def hundir(self, índice):
        hijo_izquierdo = 2 * índice + 1
        hijo_derecho = 2 * índice + 2
        índice_mayor = índice

        if hijo_izquierdo < self.size and self.heap[hijo_izquierdo] > self.heap[índice_mayor]:
            índice_mayor = hijo_izquierdo
        if hijo_derecho < self.size and self.heap[hijo_derecho] > self.heap[índice_mayor]:
            índice_mayor = hijo_derecho

        if índice_mayor != índice:
            self.heap[índice], self.heap[índice_mayor] = self.heap[índice_mayor], self.heap[índice]
            self.hundir(índice_mayor)
'''
    elif opcion == "ordenar y revisar(self)":
        st.write('''-  Devuelve verdadero (true) si el montículo no contiene elementos
                    -  Devuelve verdadero (true) si el montículo no puede almacenar más elementos
                    -  Devuelve la cantidad de elementos del montículo''', 
                unsafe_allow_html=True)
        code = '''
            def montículo_vacio(self):
        return self.size == 0

    def montículo_lleno(self):
        return self.size == len(self.heap)

    def tamaño(self):
        return self.size'''

    elif opcion == "monticulizar(self)":
        st.write(' Convierte un vector de elementos en un montículo',unsafe_allow_html=True)
        code = '''
           @classmethod
    def monticulizar(cls, elementos):
        tamaño = len(elementos)
        monticulo = cls(tamaño)
        monticulo.heap = elementos
        monticulo.size = tamaño

        for i in range(tamaño // 2 - 1, -1, -1):
            monticulo.hundir(i)

        return monticulo'''
    elif opcion == "Codigo Completo":
        code = '''
           class Monticulo:
    def __init__(self, tamaño):
        self.heap = [None] * tamaño
        self.size = 0

    def crear_monticulo(self, tamaño):
        self.heap = [None] * tamaño
        self.size = 0

    def agregar(self, dato):
        if self.size >= len(self.heap):
            # El montículo está lleno
            return
        self.heap[self.size] = dato
        self.flotar(self.size)
        self.size += 1

    def quitar(self):
        if self.size == 0:
            # El montículo está vacío
            return None
        dato = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.hundir(0)
        return dato

    def flotar(self, índice):
        padre = (índice - 1) // 2
        while índice > 0 and self.heap[índice] > self.heap[padre]:
            self.heap[índice], self.heap[padre] = self.heap[padre], self.heap[índice]
            índice = padre
            padre = (índice - 1) // 2

    def hundir(self, índice):
        hijo_izquierdo = 2 * índice + 1
        hijo_derecho = 2 * índice + 2
        índice_mayor = índice

        if hijo_izquierdo < self.size and self.heap[hijo_izquierdo] > self.heap[índice_mayor]:
            índice_mayor = hijo_izquierdo
        if hijo_derecho < self.size and self.heap[hijo_derecho] > self.heap[índice_mayor]:
            índice_mayor = hijo_derecho

        if índice_mayor != índice:
            self.heap[índice], self.heap[índice_mayor] = self.heap[índice_mayor], self.heap[índice]
            self.hundir(índice_mayor)

    def montículo_vacio(self):
        return self.size == 0

    def montículo_lleno(self):
        return self.size == len(self.heap)

    def tamaño(self):
        return self.size

    @classmethod
    def monticulizar(cls, elementos):
        tamaño = len(elementos)
        monticulo = cls(tamaño)
        monticulo.heap = elementos
        monticulo.size = tamaño

        for i in range(tamaño // 2 - 1, -1, -1):
            monticulo.hundir(i)

        return monticulo'''
    st.code(code, language='python')