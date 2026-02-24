class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triángulo de Pascal, etc.
    """

    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.

        Args:
            n (int): Posición en la secuencia (empezando desde 0)

        Returns:
            int | None: El n-ésimo número de Fibonacci, o None si n es negativo
        """
        if n < 0:
            return None

        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.

        Args:
            n (int): Cantidad de números a generar

        Returns:
            list | None: Lista con los primeros n números de Fibonacci (o None si n es negativo)
        """
        if n < 0:
            return None

        resultado = []
        a, b = 0, 1
        for _ in range(n):
            resultado.append(a)
            a, b = b, a + b
        return resultado

    def es_primo(self, n):
        """
        Verifica si un número es primo.

        Args:
            n (int): Número a verificar

        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.

        Args:
            n (int): Límite superior para generar primos

        Returns:
            list: Lista de números primos hasta n
        """
        if n < 2:
            return []
        primos = []
        for x in range(2, n + 1):
            if self.es_primo(x):
                primos.append(x)
        return primos

    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).

        Args:
            n (int): Número a verificar

        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n <= 1:
            return False

        suma = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                suma += i
                otro = n // i
                if otro != i:
                    suma += otro
            i += 1

        return suma == n

    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.

        Args:
            filas (int): Número de filas a generar

        Returns:
            list | None: Triángulo de Pascal, o None si filas es negativo
        """
        if filas < 0:
            return None
        if filas == 0:
            return []

        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        """
        Calcula el factorial de un número.

        Args:
            n (int): Número para calcular su factorial

        Returns:
            int | None: El factorial de n, o None si n es negativo
        """
        if n < 0:
            return None
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.

        Args:
            a (int): Primer número
            b (int): Segundo número

        Returns:
            int: El máximo común divisor de a y b
        """
        a = abs(a)
        b = abs(b)
        while b != 0:
            a, b = b, a % b
        return a

    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.

        Args:
            a (int): Primer número
            b (int): Segundo número

        Returns:
            int: El mínimo común múltiplo de a y b
        """
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.

        Args:
            n (int): Número para sumar sus dígitos

        Returns:
            int: La suma de los dígitos de n
        """
        n = abs(n)
        suma = 0
        for ch in str(n):
            suma += int(ch)
        return suma

    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong.

        Args:
            n (int): Número a verificar

        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        if n < 0:
            return False

        s = str(n)
        p = len(s)
        total = 0
        for ch in s:
            total += int(ch) ** p
        return total == n

    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).

        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada

        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        if not isinstance(matriz, list) or len(matriz) == 0:
            return False

        n = len(matriz)
        if any((not isinstance(fila, list)) or len(fila) != n for fila in matriz):
            return False

        objetivo = sum(matriz[0])

        # Filas
        for fila in matriz:
            if sum(fila) != objetivo:
                return False

        # Columnas
        for j in range(n):
            suma_col = 0
            for i in range(n):
                suma_col += matriz[i][j]
            if suma_col != objetivo:
                return False

        # Diagonales
        suma_diag1 = 0
        suma_diag2 = 0
        for i in range(n):
            suma_diag1 += matriz[i][i]
            suma_diag2 += matriz[i][n - 1 - i]
        if suma_diag1 != objetivo or suma_diag2 != objetivo:
            return False

        return True