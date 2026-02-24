class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.

        Args:
            celsius (float): Temperatura en grados Celsius

        Returns:
            float: Temperatura en grados Fahrenheit

        Fórmula: F = (C × 9/5) + 32

        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        return (celsius * 9 / 5) + 32

    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.

        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit

        Returns:
            float: Temperatura en grados Celsius

        Fórmula: C = (F - 32) × 5/9

        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        return (fahrenheit - 32) * 5 / 9

    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.

        Args:
            metros (float): Distancia en metros

        Returns:
            float: Distancia en pies

        Factor: 1 metro = 3.28084 pies

        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        return metros * 3.28084

    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.

        Args:
            pies (float): Distancia en pies

        Returns:
            float: Distancia en metros

        Factor: 1 pie = 0.3048 metros

        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
        return pies * 0.3048

    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.

        Args:
            decimal (int): Número decimal (positivo)

        Returns:
            str: Representación binaria como string

        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """
        if not isinstance(decimal, int):
            raise TypeError("El número decimal debe ser un entero.")
        if decimal < 0:
            raise ValueError("El número decimal debe ser positivo.")

        return bin(decimal)[2:]  # quita el prefijo 0b

    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.

        Args:
            binario (str): Representación binaria como string

        Returns:
            int: Número decimal

        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
        if not isinstance(binario, str):
            raise TypeError("El binario debe ser un string.")

        b = binario.strip()
        if b == "":
            raise ValueError("Binario vacío.")
        if any(ch not in "01" for ch in b):
            raise ValueError("Binario inválido. Solo puede contener 0 y 1.")

        return int(b, 2)

    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.

        Args:
            numero (int): Número decimal entre 1 y 3999

        Returns:
            str: Número romano

        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        if not isinstance(numero, int):
            raise TypeError("El número debe ser un entero.")
        if not (1 <= numero <= 3999):
            raise ValueError("El número debe estar entre 1 y 3999.")

        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
        ]

        res = []
        n = numero
        for valor, simbolo in valores:
            while n >= valor:
                res.append(simbolo)
                n -= valor

        return "".join(res)

    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.

        Args:
            romano (str): Número romano válido

        Returns:
            int: Número decimal

        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        if not isinstance(romano, str):
            raise TypeError("El romano debe ser un string.")

        r = romano.strip().upper()
        if r == "":
            raise ValueError("Romano vacío.")

        valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        i = 0
        while i < len(r):
            if r[i] not in valores:
                raise ValueError("Número romano inválido.")

            actual = valores[r[i]]
            if i + 1 < len(r) and r[i + 1] in valores and actual < valores[r[i + 1]]:
                total += valores[r[i + 1]] - actual
                i += 2
            else:
                total += actual
                i += 1

        # Validación: si no es forma romana canónica, lo marcamos como inválido
        if not (1 <= total <= 3999):
            raise ValueError("Número romano fuera de rango (1-3999).")

        if self.decimal_a_romano(total) != r:
            raise ValueError("Número romano inválido.")

        return total

    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.

        Args:
            texto (str): Texto a convertir (letras y números)

        Returns:
            str: Código Morse separado por espacios

        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        if not isinstance(texto, str):
            raise TypeError("El texto debe ser un string.")

        morse_map = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
            "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
            "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
            "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
            "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
            "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        }

        salida = []
        for ch in texto.upper():
            if ch == " ":
                salida.append("/")  # separador de palabras
            elif ch in morse_map:
                salida.append(morse_map[ch])
            else:
                raise ValueError(f"Carácter no soportado: {ch}")

        return " ".join(salida)

    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.

        Args:
            morse (str): Código Morse separado por espacios

        Returns:
            str: Texto decodificado

        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        if not isinstance(morse, str):
            raise TypeError("El morse debe ser un string.")

        # ✅ CAMBIO: si viene vacío, debe devolver vacío (según el test)
        morse_limpio = morse.strip()
        if morse_limpio == "":
            return ""

        morse_map = {
            ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
            "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
            "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
            ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
            "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
            "--..": "Z",
            "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
            ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
        }

        tokens = morse_limpio.split()

        salida = []
        for t in tokens:
            if t == "/":
                salida.append(" ")
            elif t in morse_map:
                salida.append(morse_map[t])
            else:
                raise ValueError(f"Código Morse inválido: {t}")

        return "".join(salida)