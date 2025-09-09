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

    def fichas_totales(self, tablero) -> int:
        """
        Devuelve el total de fichas del jugador en el tablero,
        incluyendo en agujas, barra y retiradas.
        """
        return tablero.total_fichas(self.__color__)

    def tiene_en_barra(self, tablero) -> bool:
        """True si el jugador tiene fichas en la barra."""
        return tablero.fichas_en_barra(self.__color__) > 0

    def __str__(self) -> str:
        return f"Jugador {self.__nombre__} ({self.__color__}, dir={self.__direccion__})"
