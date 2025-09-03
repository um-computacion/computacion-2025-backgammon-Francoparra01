import random

class Dados:
    def __init__(self, rng: random.Random | None = None):
        """
        rng: generador de números aleatorios inyectable (útil para tests).
        Si no se pasa, usa random.Random() por defecto.
        """
        self.__rng__ = rng or random.Random()

    def tirar(self) -> tuple[int, int]:
        """Devuelve una tirada de dos dados de 6 caras: (d1, d2)."""
        d1 = self.__rng__.randint(1, 6)
        d2 = self.__rng__.randint(1, 6)
        return d1, d2

    @staticmethod
    def expandir(d1: int, d2: int) -> list[int]:
        """
        Si hay dobles, se expanden a cuatro movimientos iguales.
        Ej: (3,3) -> [3,3,3,3]
        Si no, queda la pareja original.
        Ej: (2,5) -> [2,5]
        """
        if d1 == d2:
            return [d1, d1, d1, d1]
        return [d1, d2]
