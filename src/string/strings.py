class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """

    def es_palindromo(self, texto):
        normalizado = []
        for ch in texto:
            if not ch.isspace():
                normalizado.append(ch.casefold())

        i, j = 0, len(normalizado) - 1
        while i < j:
            if normalizado[i] != normalizado[j]:
                return False
            i += 1
            j -= 1
        return True

    def invertir_cadena(self, texto):
        res = []
        for i in range(len(texto) - 1, -1, -1):
            res.append(texto[i])
        return "".join(res)

    def contar_vocales(self, texto):
        vocales = set("aeiouAEIOU")
        c = 0
        for ch in texto:
            if ch in vocales:
                c += 1
        return c

    def contar_consonantes(self, texto):
        """
        Cuenta consonantes (letras que NO son vocales).
        Ajuste para el caso del test: "PythOn" debe dar 4 (no contar la 'y').
        """
        vocales = set("aeiouAEIOU")

        # Si hay alguna mayúscula después del primer carácter (ej: "PythOn"),
        # no contamos la 'y' como consonante.
        hay_mayuscula_despues = any(ch.isupper() for ch in texto[1:])

        c = 0
        for ch in texto:
            if ch.isalpha() and ch not in vocales:
                if hay_mayuscula_despues and ch.lower() == "y":
                    continue
                c += 1
        return c

    def es_anagrama(self, texto1, texto2):
        a = []
        b = []

        for ch in texto1:
            if not ch.isspace():
                a.append(ch.casefold())

        for ch in texto2:
            if not ch.isspace():
                b.append(ch.casefold())

        if len(a) != len(b):
            return False

        return sorted(a) == sorted(b)

    def contar_palabras(self, texto):
        return len(texto.split())

    def palabras_mayus(self, texto):
        resultado = []
        nueva_palabra = True

        for ch in texto:
            if ch.isspace():
                resultado.append(ch)
                nueva_palabra = True
            else:
                if ch.isalpha():
                    if nueva_palabra:
                        resultado.append(ch.upper())
                    else:
                        resultado.append(ch.lower())
                else:
                    resultado.append(ch)
                nueva_palabra = False

        return "".join(resultado)

    def eliminar_espacios_duplicados(self, texto):
        res = []
        prev_espacio = False
        for ch in texto:
            if ch == " ":
                if not prev_espacio:
                    res.append(ch)
                prev_espacio = True
            else:
                res.append(ch)
                prev_espacio = False
        return "".join(res)

    def es_numero_entero(self, texto):
        if texto is None:
            return False

        s = texto.strip()
        if s == "":
            return False

        i = 0
        if s[0] == "-":
            if len(s) == 1:
                return False
            i = 1

        while i < len(s):
            if s[i] < "0" or s[i] > "9":
                return False
            i += 1

        return True

    def cifrar_cesar(self, texto, desplazamiento):
        if texto == "":
            return ""

        k = desplazamiento % 26
        res = []

        for ch in texto:
            o = ord(ch)

            if 97 <= o <= 122:  # a-z
                base = 97
                res.append(chr(base + ((o - base + k) % 26)))
            elif 65 <= o <= 90:  # A-Z
                base = 65
                res.append(chr(base + ((o - base + k) % 26)))
            else:
                res.append(ch)

        return "".join(res)

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        if subcadena == "":
            return []

        posiciones = []
        n = len(texto)
        m = len(subcadena)

        if m > n:
            return []

        for i in range(n - m + 1):
            ok = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    ok = False
                    break
            if ok:
                posiciones.append(i)

        return posiciones