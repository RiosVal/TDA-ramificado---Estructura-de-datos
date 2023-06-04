class Monticulo:
    def __init__(self):
        self.elementos = []  # Lista para almacenar los elementos del montículo

    def esta_vacio(self):
        return len(self.elementos) == 0  # Verificar si el montículo está vacío

    def insertar(self, elemento, prioridad):
        self.elementos.append((elemento, prioridad))  # Agregar el elemento al final de la lista
        self.subir_elemento(len(self.elementos) - 1)  # Realizar el proceso de subir el elemento en el montículo

    def eliminar_minimo(self):
        if self.esta_vacio():
            return None

        minimo = self.elementos[0]  # Obtener el elemento mínimo (raíz del montículo)
        ultimo = self.elementos.pop()  # Eliminar el último elemento de la lista

        if not self.esta_vacio():
            self.elementos[0] = ultimo  # Colocar el último elemento en la raíz
            self.bajar_elemento(0)  # Realizar el proceso de bajar el elemento en el montículo

        return minimo[0]  # Devolver el elemento mínimo

    def subir_elemento(self, indice):
        while indice > 0:
            indice_padre = (indice - 1) // 2  # Calcular el índice del padre

            if self.elementos[indice][1] >= self.elementos[indice_padre][1]:
                break  # Si la prioridad del elemento es mayor o igual que la del padre, finalizar

            # Intercambiar el elemento con su padre
            self.elementos[indice], self.elementos[indice_padre] = self.elementos[indice_padre], self.elementos[indice]
            indice = indice_padre  # Actualizar el índice con el del padre

    def bajar_elemento(self, indice):
        tamanio = len(self.elementos)

        while indice < tamanio:
            hijo_izquierdo = 2 * indice + 1  # Calcular el índice del hijo izquierdo
            hijo_derecho = 2 * indice + 2  # Calcular el índice del hijo derecho
            indice_minimo = indice

            if hijo_izquierdo < tamanio and self.elementos[hijo_izquierdo][1] < self.elementos[indice_minimo][1]:
                indice_minimo = hijo_izquierdo  # Actualizar el índice mínimo si el hijo izquierdo tiene una prioridad menor

            if hijo_derecho < tamanio and self.elementos[hijo_derecho][1] < self.elementos[indice_minimo][1]:
                indice_minimo = hijo_derecho  # Actualizar el índice mínimo si el hijo derecho tiene una prioridad menor

            if indice_minimo == indice:
                break  # Si el índice mínimo es igual al índice actual, finalizar

            # Intercambiar el elemento con el hijo de menor prioridad
            self.elementos[indice], self.elementos[indice_minimo] = self.elementos[indice_minimo], self.elementos[indice]
            indice = indice_minimo  # Actualizar el índice con el del hijo de menor prioridad

    def obtener_minimo(self):
        if self.esta_vacio():
            return None

        return self.elementos[0][0]  # Devolver el elemento mínimo

    def generar_lista_priorizada(self):
        lista_priorizada = sorted(self.elementos, key=lambda x: (x[1], x[0]['hora'], x[0]['fecha']))  # Ordenar los elementos por prioridad, hora y fecha
        return [elemento[0] for elemento in lista_priorizada]  # Devolver solo los elementos sin la prioridad
    