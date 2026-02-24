import math


class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        """
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)

    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.
        """
        if not numeros:
            return 0

        ordenados = sorted(numeros)
        n = len(ordenados)
        mid = n // 2

        if n % 2 == 1:
            return float(ordenados[mid])
        else:
            return (ordenados[mid - 1] + ordenados[mid]) / 2

    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        """
        if not numeros:
            return None

        conteos = {}
        for x in numeros:
            conteos[x] = conteos.get(x, 0) + 1

        max_freq = -1
        mejor = None
        for x in numeros:  # respeta "primer valor encontrado" en caso de empate
            freq = conteos[x]
            if freq > max_freq:
                max_freq = freq
                mejor = x
        return mejor

    def varianza(self, numeros):
        """
        Calcula la varianza poblacional de una lista de números.
        """
        if not numeros:
            return 0

        mu = self.promedio(numeros)
        suma = 0
        for x in numeros:
            suma += (x - mu) ** 2
        return suma / len(numeros)

    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar poblacional de una lista de números.
        """
        return math.sqrt(self.varianza(numeros))

    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        """
        if not numeros:
            return 0
        return max(numeros) - min(numeros)