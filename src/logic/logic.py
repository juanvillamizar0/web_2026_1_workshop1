class Logica:
    """
    Operaciones lógicas básicas.
    Los métodos devuelven siempre True/False (booleano).
    """

    def AND(self, a, b):
        return bool(a) and bool(b)

    def OR(self, a, b):
        return bool(a) or bool(b)

    def NOT(self, a):
        return not bool(a)

    def XOR(self, a, b):
        return bool(a) ^ bool(b)

    def NAND(self, a, b):
        return not (bool(a) and bool(b))

    def NOR(self, a, b):
        return not (bool(a) or bool(b))

    def XNOR(self, a, b):
        return not (bool(a) ^ bool(b))