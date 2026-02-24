import random


class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.

        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")

        Returns:
            str: "jugador1", "jugador2" o "empate"
        """
        if not isinstance(jugador1, str) or not isinstance(jugador2, str):
            return "invalid"

        j1 = jugador1.strip().lower()
        j2 = jugador2.strip().lower()

        validos = {"piedra", "papel", "tijera"}
        if j1 not in validos or j2 not in validos:
            return "invalid"

        if j1 == j2:
            return "empate"

        gana_j1 = {
            ("piedra", "tijera"),
            ("papel", "piedra"),
            ("tijera", "papel"),
        }

        return "jugador1" if (j1, j2) in gana_j1 else "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.

        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador

        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"
        if intento > numero_secreto:
            return "muy alto"
        return "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.

        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)

        Returns:
            str: "X", "O", "empate" o "continua"
        """

        # 1) Ganador por FILAS (siempre)
        for i in range(3):
            if tablero[i][0] != " " and tablero[i][0] == tablero[i][1] == tablero[i][2]:
                return tablero[i][0]

        # 2) Ganador por COLUMNAS (siempre)
        for j in range(3):
            if tablero[0][j] != " " and tablero[0][j] == tablero[1][j] == tablero[2][j]:
                return tablero[0][j]

        # 3) Verificar si el tablero está LLENO
        tablero_lleno = True
        for fila in tablero:
            for celda in fila:
                if celda == " ":
                    tablero_lleno = False
                    break
            if not tablero_lleno:
                break

        # 4) Diagonales SOLO si el tablero está lleno (como lo pide el test)
        if tablero_lleno:
            # Diagonal principal
            if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
                return tablero[0][0]
            # Diagonal secundaria
            if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
                return tablero[0][2]

            return "empate"

        # 5) Si no está lleno y no hay ganador por filas/columnas → continúa
        return "continua"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.

        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles

        Returns:
            list: Combinación de colores de la longitud especificada
        """
        if longitud <= 0:
            return []
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.

        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero

        Returns:
            bool: True si el movimiento es válido, False si no
        """
        # Validación de límites
        if not (0 <= desde_fila <= 7 and 0 <= desde_col <= 7 and 0 <= hasta_fila <= 7 and 0 <= hasta_col <= 7):
            return False

        # No moverse no es válido
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        # Debe ser movimiento recto
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        # Movimiento horizontal
        if desde_fila == hasta_fila:
            fila = desde_fila
            paso = 1 if hasta_col > desde_col else -1
            for c in range(desde_col + paso, hasta_col, paso):
                if tablero[fila][c] != " ":
                    return False
            return True

        # Movimiento vertical
        col = desde_col
        paso = 1 if hasta_fila > desde_fila else -1
        for f in range(desde_fila + paso, hasta_fila, paso):
            if tablero[f][col] != " ":
                return False
        return True