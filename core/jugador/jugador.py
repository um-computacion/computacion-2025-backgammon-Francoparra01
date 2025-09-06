class Jugador:
    def __init__(self, nombre: str, color: str, direccion: int):
        """
        nombre: identificador del jugador.
        color: "blanco" o "negro".
        direccion: 1 si avanza de izquierda a derecha, -1 al revés.
        """
        self.__nombre__ = nombre
        self.__color__ = color
        self.__direccion__ = direccion

    def nombre(self) -> str:
        return self.__nombre__

    def color(self) -> str:
        return self.__color__

    def direccion(self) -> int:
        return self.__direccion__
